*** Settings ***
Resource           variable.robot
Library             SeleniumLibrary
Library             custom_library.py

*** Keywords ***

User Opens Facebook
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Capture Page Screenshot    Facebook_Login_Page.png

User Enters Login Credentials
    [Arguments]    ${username}    ${password}    ${email_xpath}    ${password_xpath}
    Input Text    xpath:${email_xpath}    ${username}
    Input Password    xpath:${password_xpath}    ${password}
    Capture Page Screenshot    Facebook_Credentials_Entered.png

User Clicks Login Button
    [Arguments]    ${login_xpath}
    Click Element    xpath:${login_xpath}
    Capture Page Screenshot    Facebook_Login_Clicked.png

Verify Facebook Login Result
    Wait Until Page Does Not Contain Element    xpath:${fb_welcome_page_logo_xpath}    10s

Capture Login Screenshot
    Capture Page Screenshot    Facebook_Login_Result.png