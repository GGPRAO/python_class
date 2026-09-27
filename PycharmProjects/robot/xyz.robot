*** Settings ***
Library    SeleniumLibrary

Force Tags    mahesh-123


*** Variables ***
${chrome}    chrome
${edge}    edge
${fb}    https://www.facebook.com
${gg}    https://www.google.com

@{browssers}    chrome    edge

&{browser}    chrome=chrome    edge=edge

*** Keywords ***
Open Browser TO Facebook
    open Browser    ${fb}    ${browssers}[0]


*** Test Cases ***
open facebook
    [Tags]    regression
    Open Browser TO Facebook
    Capture Page Screenshot
    Close Browser


