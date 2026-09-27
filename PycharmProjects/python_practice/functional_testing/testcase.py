import pandas as pd

def generate_automation_sheet(input_file, output_file):
    # Load your basic requirement sheet
    df = pd.read_csv(input_file)

    # Placeholders for generated content
    scenarios = []
    test_cases = []
    queries = []

    for index, row in df.iterrows():
        logic = row['trans_logic'].upper()
        src_col = row['src_column']
        tgt_col = row['tgt_column']
        src_tab = row['src_table']
        tgt_tab = row['tgt_table']

        # Logic Engine: Auto-generating content based on the transformation type
        if "SURROGATE_KEY" in logic:
            scenarios.append("Primary Key Uniqueness")
            test_cases.append(f"Ensure {tgt_col} has no duplicates or nulls")
            queries.append(f"SELECT {tgt_col}, COUNT(*) FROM {tgt_tab} GROUP BY 1 HAVING COUNT(*) > 1;")

        elif "MAPPING" in logic:
            scenarios.append("Value Transformation")
            test_cases.append(f"Validate {src_col} correctly maps to {tgt_col}")
            queries.append(f"SELECT DISTINCT {tgt_col} FROM {tgt_tab};")

        elif "YYYYMMDD" in logic:
            scenarios.append("Date Format Conversion")
            test_cases.append(f"Check if {tgt_col} is in numeric YYYYMMDD format")
            queries.append(f"SELECT {tgt_col} FROM {tgt_tab} WHERE LENGTH(CAST({tgt_col} AS STRING)) != 8;")

        elif "MULTIPLY" in logic:
            scenarios.append("Calculated Field Validation")
            test_cases.append(f"Verify {tgt_col} matches calculation logic")
            queries.append(f"SELECT * FROM {tgt_tab} T JOIN {src_tab} S ON T.ID = S.ID WHERE T.{tgt_col} != (S.UNIT_PRICE * S.QTY);")

        elif "UPPER_TRIM" in logic:
            scenarios.append("Data Cleansing")
            test_cases.append(f"Ensure {tgt_col} is uppercase with no whitespace")
            queries.append(f"SELECT {tgt_col} FROM {tgt_tab} WHERE {tgt_col} != UPPER(TRIM({tgt_col}));")

        else:
            scenarios.append("Data Integrity")
            test_cases.append("Direct mapping check")
            queries.append(f"SELECT count(*) FROM (SELECT {src_col} FROM {src_tab} EXCEPT SELECT {tgt_col} FROM {tgt_tab});")

    # Add the new columns to the dataframe
    df['test_scenario'] = scenarios
    df['test_case'] = test_cases
    df['validation_query'] = queries

    # Export to a new CSV
    df.to_csv(output_file, index=False)
    print(f"Automation Complete! File saved as: {output_file}")

# Run the function
generate_automation_sheet('requirements.csv', 'automated_testing_sheet.csv')