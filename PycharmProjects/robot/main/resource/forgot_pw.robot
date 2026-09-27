*** Keywords ***

forget username
    [Documentation]    This test case verifies the functionality of the "Forget Password" feature.
    [Tags]    forget_password
    Open Browser    ${FORGET_PASSWORD_URL}    ${BROWSER}
    Input Text    id=username_field    ${USERNAME}
    Click Button    id=submit_button
    Wait Until Page Contains Element    id=confirmation_message
    Element Should Contain    id=confirmation_message    A password reset link has been sent to your email.
    Close Browser