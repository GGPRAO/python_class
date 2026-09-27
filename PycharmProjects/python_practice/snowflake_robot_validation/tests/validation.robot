*** Settings ***
Library    ../libraries/snowflake_lib.py    WITH NAME    Snowflake

*** Variables ***
${ACCOUNT}     OSYXZVF-KO97206
${USER}        GGPRAO
${PASSWORD}    HappyDays@1992
${ROLE}        ACCOUNTADMIN
${WAREHOUSE}   COMPUTE_WH
${DATABASE}    SIT

${SRC_SCHEMA}  SRC
${TGT_SCHEMA}  TGT
${YAML_FILE}   ../resources/tables.yml
${CSV_FILE}    validation_results.csv

*** Test Cases ***
Snowflake Data Validation
    Snowflake.Connect To Snowflake    ${ACCOUNT}    ${USER}    ${PASSWORD}    ${ROLE}    ${WAREHOUSE}    ${DATABASE}
    Snowflake.Run Validations         ${SRC_SCHEMA}    ${TGT_SCHEMA}    ${YAML_FILE}    ${CSV_FILE}
    Snowflake.Close Connection
