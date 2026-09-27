*** Keywords ***
register user
    [Documentation]    This test case verifies the functionality of the "Register User" feature.
    [Tags]    register_user
    Open Browser    ${REGISTER_URL}    ${BROWSER}
    Input Text    id=username_field    ${USERNAME}
    Input Text    id=email_field       ${EMAIL}
    Input Text    id=password_field    ${PASSWORD}
    Click Button    id=register_button
    Wait Until Page Contains Element    id=confirmation_message
    Element Should Contain    id=confirmation_message    Registration successful. Please check your email to verify your account.
    Close Browser