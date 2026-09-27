import snowflake.connector


conn = snowflake.connector.connect(
    user
    pwd
    role
    account

)

cur = conn.cursor()


cur.execute("select * from employee")
   row = cur.fetchone()
   print(row)


