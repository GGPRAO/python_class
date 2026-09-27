*** Settings ***
Documentation       Facebook Login Automation
Library             SeleniumLibrary
Library             DataDriver    file=login_data.csv    dialect=excel
Library             custom_library.py
Resource           facebook_keywords.robot
Resource           variable.robot

Force Tags    Facebook_Login

Test Template       Facebook Login Test
Test Teardown       Close All Browsers

*** Variables ***
${URL}                          https://www.facebook.com/
${fb_welcome_page_logo_xpath}   //*[@id="mount_0_0_A8"]

*** Test Cases ***
Facebook Login with ${username}
    [Documentation]
    ...    DESCRIPTION:
    ...    Login to Facebook using credentials from CSV file.
    ...
    ...    PRE-REQUISITE:
    ...    1. Chrome browser should be installed.
    ...    2. Login data should be available in login_data.csv.
    ...
    ...    EXPECTED RESULTS:
    ...    1. Facebook login page should be displayed.
    ...    2. Login should be validated based on the result.
    [Tags]    UI    Login    Regression
    ${username}    ${password}    ${email_xpath}    ${password_xpath}    ${login_xpath}

*** Keywords ***
Facebook Login Test
    [Arguments]    ${username}    ${password}    ${email_xpath}    ${password_xpath}    ${login_xpath}
    Given User Opens Facebook
    When User Enters Login Credentials    ${username}    ${password}    ${email_xpath}    ${password_xpath}
    And User Clicks Login Button    ${login_xpath}
    Then Verify Facebook Login Result
    And Capture Login Screenshot