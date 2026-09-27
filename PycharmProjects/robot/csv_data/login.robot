*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=login_data.csv    dialect=excel
Test Template    Facebook Login Test
Library    custom_library.py


*** Variables ***
${URL}    https://www.facebook.com/

${fb_welcome_page_logo_xpath}    //*[@id="mount_0_0_A8"]

*** Test Cases ***
Facebook Login with ${username}
    ${username}    ${password}    ${email_xpath}    ${password_xpath}    ${login_xpath}

*** Keywords ***
Facebook Login Test
    [Arguments]    ${username}    ${password}    ${email_xpath}    ${password_xpath}    ${login_xpath}
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Text    xpath:${email_xpath}    ${username}
    sleep    5s
    Input Password    xpath:${password_xpath}    ${password}
    sleep    5s
    Click Element    xpath:${login_xpath}
    sleep    5s
    Capture Page Screenshot
    Wait Until I Close Browser
    Wait Until Page Contains    ${fb_welcome_page_logo_xpath}
#    Close Browser