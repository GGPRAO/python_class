*** Settings ***
Resource    ../resource/login.robot
Resource    ../resource/forget_username.robot
Resource    ../resource/forgot_pw.robot
Resource    ../resource/resister.robot
Resource    ../resource/welcome.robot


*** Test Cases ***

verify login page
    login

verfify forget  username page
    forget username
