*** Keywords ***
login to facebook
    Open Browser    ${fbase_url}   ${browser}
    Input Text    name=email    ${use_details}[name]
    Input Text    name=pass    ${use_details}[password]
    Click Button    name=login