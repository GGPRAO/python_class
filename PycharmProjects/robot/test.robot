*** Settings ***
Library    SeleniumLibrary

Force Tags    gopi-123    mahesh-123


*** Variables ***
${chrome}    chrome
${edge}    edge
${fb}    https://www.facebook.com
${gg}    https://www.google.com

@{browssers}    chrome    edge

&{browser}    chrome=chrome    edge=edge

*** Keywords ***

*** Test Cases ***
open facebook
    [Tags]    regression
    open Browser    ${fb}    ${browssers}[0]
    Capture Page Screenshot
    Close Browser

Open google
    Open Browser    ${gg}    ${browser}[edge]
    Maximize Browser Window
    Sleep    5s
    Capture Page Screenshot
    Close Browser
