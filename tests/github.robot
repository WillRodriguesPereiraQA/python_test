**Settings**
Resource        ../../resources/helpers.robot
Test Setup      Open Session
Test Teardown   Close Session

**Test Cases**
Print the first 300 characters of the README
    [tags]  github
    Given that the I am searching for "react" on github
    And select the advanced search
    And set up the language "JavaScript"
    And With this many stars ">45"
    And With this license "Boost Software License 1.0"
    And With this many followers ">50"
    And hit the search
    And check if there is only one repository as result
    When open the repository
    And open the README
    Then the first 300 characters are displayed
    
   
