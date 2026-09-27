*** Settings ***
Library    SeleniumLibrary
Resource    login.robot


Suite Setup    Login To Facebook

*** Variables ***
${name}    Mahesh
${password}    Mahesh@123

@{use_details}    Mahesh    Mahesh@123

&{user_details}    name=Mahesh    password=Mahesh@123

${fbase_url}    https://www.facebook.com/
${browser}    chrome



*** Keywords ***


*** Test Cases ***
