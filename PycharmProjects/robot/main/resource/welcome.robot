*** Keywords ***
welcome page
    [Documentation]    This test case verifies the functionality of the "Welcome Page" feature.
    [Tags]    welcome_page
    Open Browser    ${WELCOME_URL}    ${BROWSER}
    Wait Until Page Contains Element    id=welcome_message
    Element Should Contain    id=welcome_message    Welcome to our application!
    Close Browser