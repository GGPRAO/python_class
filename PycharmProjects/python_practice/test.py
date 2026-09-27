import snowflake.connector
import csv

# --------------------
# Snowflake Connection
# --------------------
conn = snowflake.connector.connect(
    account="OSYXZVF-KO97206",
    user="GGPRAO",
    password="HappyDays@1992",
    role="ACCOUNTADMIN",
    warehouse="COMPUTE_WH",
    database="SIT"
)

cur = conn.cursor()

SRC_SCHEMA = "SRC"
TGT_SCHEMA = "TGT"
TABLE_NAME = "TEST"

# --------------------
# CSV Output
# --------------------
csv_file = "validation_results.csv"

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["TEST_NAME", "STATUS", "DETAILS", "QUERY"])

    # ==================================================
    # Test Case 1: COUNT CHECK
    # ==================================================
    src_count_query = f"SELECT COUNT(*) FROM {SRC_SCHEMA}.{TABLE_NAME}"
    tgt_count_query = f"SELECT COUNT(*) FROM {TGT_SCHEMA}.{TABLE_NAME}"

    # SRC count
    cur.execute(src_count_query)
    src_count = cur.fetchone()[0]
    writer.writerow([
        "COUNT_CHECK_SRC",
        "INFO",
        f"COUNT={src_count}",
        src_count_query
    ])

    # TGT count
    cur.execute(tgt_count_query)
    tgt_count = cur.fetchone()[0]
    writer.writerow([
        "COUNT_CHECK_TGT",
        "INFO",
        f"COUNT={tgt_count}",
        tgt_count_query
    ])

    # Count comparison result
    if src_count == tgt_count:
        writer.writerow([
            "COUNT_CHECK_RESULT",
            "PASS",
            f"SRC={src_count}, TGT={tgt_count}",
            "SRC_COUNT = TGT_COUNT"
        ])
    else:
        writer.writerow([
            "COUNT_CHECK_RESULT",
            "FAIL",
            f"SRC={src_count}, TGT={tgt_count}",
            "SRC_COUNT <> TGT_COUNT"
        ])

    # ==================================================
    # Test Case 2: MINUS CHECK (SRC - TGT)
    # ==================================================
    minus_query = f"""
    SELECT id, first_name, last_name, email, gender
    FROM {SRC_SCHEMA}.{TABLE_NAME}
    MINUS
    SELECT id, first_name, last_name, email, gender
    FROM {TGT_SCHEMA}.{TABLE_NAME}
    """

    cur.execute(minus_query)
    diff_rows = cur.fetchall()

    if len(diff_rows) == 0:
        writer.writerow([
            "MINUS_CHECK_SRC_TGT",
            "PASS",
            "No mismatched records",
            minus_query.strip()
        ])
    else:
        writer.writerow([
            "MINUS_CHECK_SRC_TGT",
            "FAIL",
            f"{len(diff_rows)} mismatched records",
            minus_query.strip()
        ])

# --------------------
# Cleanup
# --------------------
cur.close()
conn.close()

print("Validation completed. Results written to validation_results.csv")
