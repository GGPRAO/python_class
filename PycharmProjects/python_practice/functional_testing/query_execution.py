import pandas as pd
import snowflake.connector
from openpyxl import Workbook

# 1. Your Snowflake Connection Details
SNOWFLAKE_CONFIG = {
    "account": "OSYXZVF-KO97206",
    "user": "GGPRAO",
    "password": "HappyDays@1992",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "SIT",
    "schema": "PUBLIC"  # Added a default schema, change if needed
}


def run_snowflake_test_suite(input_csv, output_excel):
    # Load the requirement sheet
    df_reqs = pd.read_csv(input_csv)

    # Establish Connection
    ctx = snowflake.connector.connect(**SNOWFLAKE_CONFIG)

    summary_data = []

    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        for index, row in df_reqs.iterrows():
            # Create a clean sheet name (max 31 chars)
            sheet_name = f"{index + 1}_{row['tgt_column']}"[:31]
            query = row['validation_query']

            try:
                # Execute query directly into a Dataframe
                result_df = pd.read_sql(query, ctx)

                if result_df.empty:
                    status = "PASS"
                    fail_count = 0
                    # Create a simple Pass sheet
                    pd.DataFrame({"Status": ["PASSED"], "Result": ["All records match logic"]}).to_excel(writer,
                                                                                                         sheet_name=sheet_name,
                                                                                                         index=False)
                else:
                    status = "FAIL"
                    fail_count = len(result_df)
                    # Write the actual failing records to the sheet
                    result_df.to_excel(writer, sheet_name=sheet_name, index=False)

            except Exception as e:
                status = "ERROR"
                fail_count = "N/A"
                pd.DataFrame({"Error": [str(e)]}).to_excel(writer, sheet_name=sheet_name, index=False)

            # Collect data for the Summary tab
            summary_data.append({
                "Test_ID": index + 1,
                "Target_Column": row['tgt_column'],
                "Scenario": row['test_scenario'],
                "Status": status,
                "Failing_Records_Count": fail_count
            })

        # Generate the Summary Sheet
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_excel(writer, sheet_name="EXECUTION_SUMMARY", index=False)

        # Move Summary to the first position
        workbook = writer.book
        summary_sheet = workbook["EXECUTION_SUMMARY"]
        workbook._sheets = [summary_sheet] + [s for s in workbook._sheets if s.title != "EXECUTION_SUMMARY"]

    ctx.close()
    print(f"--- Automation Finished ---")
    print(f"Results saved to: {output_excel}")


# Run the script
# Ensure your CSV filename matches 'requirements.csv'
run_snowflake_test_suite('requirements.csv', 'Snowflake_Validation_Results.xlsx')