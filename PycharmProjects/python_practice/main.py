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
    writer.writerow(["TEST_NAME", "STATUS", "DETAILS"])

    # --------------------
    # Test Case 1: Count Check
    # --------------------
    cur.execute(f"SELECT COUNT(*) FROM {SRC_SCHEMA}.{TABLE_NAME}")
    src_count = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM {TGT_SCHEMA}.{TABLE_NAME}")
    tgt_count = cur.fetchone()[0]

    if src_count == tgt_count:
        writer.writerow(["COUNT_CHECK", "PASS", f"SRC={src_count}, TGT={tgt_count}"])
    else:
        writer.writerow(["COUNT_CHECK", "FAIL", f"SRC={src_count}, TGT={tgt_count}"])

    # --------------------
    # Test Case 2: MINUS Check
    # --------------------
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
        writer.writerow(["MINUS_CHECK", "PASS", "No mismatched records"])
    else:
        writer.writerow(["MINUS_CHECK", "FAIL", f"{len(diff_rows)} mismatched records"])

# --------------------
# Cleanup
# --------------------
cur.close()
conn.close()

print("Validation completed. Results written to validation_results.csv")
