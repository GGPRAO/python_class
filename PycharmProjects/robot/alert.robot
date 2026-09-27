*** Settings ***
Library    SeleniumLibrary
Resource    browser.robot



*** Variables ***
${URL}    https://the-internet.herokuapp.com/javascript_alerts


*** Test Cases ***

Simple Alert Test1
    [Tags]    
    Open Browser    ${URL}    chrome
    Click Element    //*[@id="content"]/div/ul/li[1]/button
    Handle Alert    accept
    Sleep    10s
    Capture Page Screenshot    screen1.PNG
    Close Browser



Simple Alert Test2
    Open Browser    ${URL}    chrome
    Click Element    //*[@id="content"]/div/ul/li[2]/button
    Handle Alert    accept
    Sleep    10s
    Capture Page Screenshot    screen2.PNG
    Close Browser


Simple Alert Test3
    Open Browser    ${URL}    chrome
    Click Element    //*[@id="content"]/div/ul/li[2]/button
    Handle Alert    dismiss
    Sleep    10s
    Capture Page Screenshot    screen3.PNG
    Close Browser

Simple Alert Test4
    Open Browser    ${URL}    chrome
    Click Element    //*[@id="content"]/div/ul/li[3]/button
    Input Text Into Alert    Gopi
    Sleep    10s
    Capture Page Screenshot    screen4.PNG
    Close Browser


Simple Alert Test5
    Open Browser    ${URL}    chrome
    Click Element    //*[@id="content"]/div/ul/li[3]/button
    Input Text Into Alert    Gopi    Dismiss
    Sleep    10s
    Capture Page Screenshot    screen5.PNG
    Close Browser

one
    google bowser launch
    
    Capture Element Screenshot    //*[@id="gb"]/div[1]/div[1]/a    one.png
    facebook bowser launch

