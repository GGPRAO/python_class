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
Open google
    Open Browser    ${gg}    ${browser}[edge]
    Maximize Browser Window
    Sleep    5s
    Capture Page Screenshot
    Close Browser
