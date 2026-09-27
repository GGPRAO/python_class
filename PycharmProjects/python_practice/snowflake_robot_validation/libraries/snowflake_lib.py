import snowflake.connector
import yaml
import csv
import os
from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class SnowflakeLibrary:

    def __init__(self):
        self.conn = None
        self.cur = None

    @keyword
    def connect_to_snowflake(self, account, user, password, role, warehouse, database):
        self.conn = snowflake.connector.connect(
            account=account,
            user=user,
            password=password,
            role=role,
            warehouse=warehouse,
            database=database
        )
        self.cur = self.conn.cursor()
        BuiltIn().log("Connected to Snowflake successfully.", level="INFO")

    @keyword
    def run_validations(self, src_schema, tgt_schema, yaml_path, csv_file):
        # 1. Load YAML
        if not os.path.exists(yaml_path):
            BuiltIn().fail(f"YAML file not found at: {yaml_path}")

        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)

        tables = data.get("tables", [])
        all_failures = []

        # 2. Open CSV and Start Loop
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["TABLE_NAME", "CHECK_TYPE", "STATUS", "DETAILS", "QUERY"])

            for table in tables:
                table_name = table["name"]
                columns = ", ".join(table["columns"])

                BuiltIn().log(f"--- Processing Table: {table_name} ---", level="INFO")

                # ---------- COUNT CHECK BLOCK ----------
                try:
                    src_q = f"SELECT COUNT(*) FROM {src_schema}.{table_name}"
                    tgt_q = f"SELECT COUNT(*) FROM {tgt_schema}.{table_name}"

                    self.cur.execute(src_q)
                    src_count = self.cur.fetchone()[0]

                    self.cur.execute(tgt_q)
                    tgt_count = self.cur.fetchone()[0]

                    if src_count != tgt_count:
                        msg = f"{table_name} COUNT MISMATCH: SRC={src_count}, TGT={tgt_count}"
                        writer.writerow([table_name, "COUNT", "FAIL", msg, f"{src_q} vs {tgt_q}"])
                        all_failures.append(msg)
                    else:
                        writer.writerow([table_name, "COUNT", "PASS", f"Match: {src_count}", src_q])

                except Exception as e:
                    err_msg = f"Error during COUNT check for {table_name}: {str(e)}"
                    writer.writerow([table_name, "COUNT", "ERROR", str(e), "N/A"])
                    all_failures.append(err_msg)

                # ---------- MINUS CHECK BLOCK ----------
                try:
                    minus_q = f"SELECT {columns} FROM {src_schema}.{table_name} MINUS SELECT {columns} FROM {tgt_schema}.{table_name}"

                    self.cur.execute(minus_q)
                    mismatched_rows = self.cur.fetchall()

                    if len(mismatched_rows) > 0:
                        msg = f"{table_name} DATA MISMATCH: {len(mismatched_rows)} extra records in Source"
                        writer.writerow([table_name, "DATA_DIFF", "FAIL", msg, minus_q])
                        all_failures.append(msg)
                    else:
                        writer.writerow([table_name, "DATA_DIFF", "PASS", "Data matches", minus_q])

                except Exception as e:
                    err_msg = f"Error during DATA check for {table_name}: {str(e)}"
                    writer.writerow([table_name, "DATA_DIFF", "ERROR", str(e), minus_q])
                    all_failures.append(err_msg)

        # 3. Final Decision
        if all_failures:
            summary = "\n".join(all_failures)
            BuiltIn().fail(f"Validation completed with failures:\n{summary}")
        else:
            BuiltIn().log("All tables in YAML validated successfully.", level="INFO")

    @keyword
    def close_connection(self):
        if self.cur: self.cur.close()
        if self.conn: self.conn.close()
        BuiltIn().log("Snowflake connection closed.", level="INFO")