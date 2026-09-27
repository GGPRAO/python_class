*** Settings ***
Documentation      Study Setup Jira-ID: JADF-5409, JADF-4519
Test Teardown      Close all browsers
Library             OperatingSystem
Library             JSONLibrary
Library             RequestsLibrary
Library             SeleniumLibrary
Resource           ../Support.robot
Resource           ../PO/PO_login.robot
Resource           ../PO/PO_task.robot
Resource           ../PO/PO_menu.robot
Resource           ../PO/PO_Catalog.robot
Resource           ../PO/PO_study_setup.robot
Resource           Support/JADF_18906_Support.robot
Resource            ../RESOURCE/TestDataLoader.robot
Test Setup          Initialize Execution Context

*** Test Cases ***
# BST JADF-20219
[RGT] [V2] L1 Study Setup : Listings - Edit Listing
    [Documentation]
    ...   *DESCRIPTION:*
    ...   As a study team member, I need to Edit Listing through Listing Section in Study Setup Menu. User needs to edit table name of the record.
    ...
    ...   *PRE-REQUISITE:*
    ...   1. Data4You URL.
    ...   2. Configure Study in execution parameters before script execution.
    ...   3. Study Member have access to studies.
    ...   4. Listing record Which will be the Search criteria should be available in Application.
    ...   5. Search Criteria to Select Listing record and Updating Table name can be configured
    ...   in "Listings" Sheet in "View_Record_From_Catalog.xlsx" file.
    ...
    ...   *Test Data*
    ...    "View_Record_From_StudySetup.xlsx" should be available in the framework at bitbucket location -
    ...    "d4u_regression/test/robot_lab/d4u_app/Tests/STUDY_SETUP/Support/Configuration_Files/" before the execution begins.
    ...
    ...   *Note*
    ...     1. Make Sure to use same template and just add the values to the respective column to avoid automation fail.
    ...
    ...   *EXPECTED RESULTS:*
    ...   1. Study Setup Page Displays, Listing Section and Listing Detail should Displays.
    ...   2. Updated changes should reflect in the application for Listings section.
    ...   Labels: Automation, BST, GR2, RGT, UI, L1
    [Tags]    18906-TC40   RGT_TA_06_152026    RGT_SS_Group
#    [Setup]   Setup Search Test Case Study
    Given A Study Member login to Data4You and selects Study
    And Select Study Setup Menu
    When Enable the 'Search' option on the Study Panel
    Then Enter a search criteria with matching Study
#   And Select the Study from search results
    And Select Listings from Study Setup
    And Search The Listing
    And View Searched Listing
    And Select Edit Button
#    And Update Table Name for Selected Listing
    And Select Save Button
    And Log out from Data4You

*** Keywords ***
A Study Member login to Data4You and selects Study
    JADF_18906_Support.Study member was logged into Data4You
    JADF_18906_Support.Study member name was displayed
    JADF_18906_Support.Study from Study List selected
    JADF_18906_Support.Study Member role displayed
    log     Logged in Study Member: ${User Name}
    log     Selected Study is: ${TestStudy}
    log     Study Member Role: ${User Role}
    Capture Page Screenshot     D4U_LoggedIn.png

Select Study Setup Menu
    Study Setup Metadata Page Displayed
    Capture Page Screenshot     D4U_StudySetup.png

Enable the 'Search' option on the Study Panel
    Search Bar with Studies List is Displayed in Study Panel
    Capture Page Screenshot     D4U_SearchBarStudyPanel.png

Enter a search criteria with matching Study
    Search criteria having a match study protocol id was entered
    Log  Search criteria entered: ${Search Criteria}
    Capture Page Screenshot     D4U_SearchCriteriaMatch.png

Select the Study from search results
    Study was selected
    Lifecycle Switched to Dev
    Log  Selected Study ID: ${Select Study ID}
    Capture Page Screenshot     D4U_SelectStudyResult.png

Select Listings from Study Setup
    Listings section displayed
    Capture Page Screenshot     D4U_StudySetupListing.png

Search the Listing
    JADF_18906_Support.Results displayed for Listings Search criteria
    Capture Page Screenshot     D4U_StudySetupSearchResult.png
#   sleep     5s

View Searched Listing
    Searched Listing Detail Page was opened
    Capture Page Screenshot     D4U_SelectedRecordListingsDetailPage.png

Select Edit Button
    Record Edit Button was Selected
    Capture Page Screenshot     D4U_SelectedRecordEditButton.png

Update Table Name for Selected Listing
    Table name for selected Listing were updated
    Capture Page Screenshot     D4U_SelectedRecordlistingsUpdated.png

Select Save Button
    Selected listings were updated
    Log  Listing updated message: ${Toast_message}

Log out from Data4You
    Profile Menu items displayed
    Capture Page Screenshot     D4U_ProfileIcon.png
    Study member was logged out of Data4You
    Capture Page Screenshot     D4U_LogOut.png