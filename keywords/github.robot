***Keywords***

Given that the I am searching for "${react}" on github
    Wait Until Element is Visible       ${searchText}
    Input Text                          ${searchText}     ${react}
    Click Element                       ${searchPress}

And select the advanced search
    Scroll Element Into View            ${advancedText}
    Click Element                       ${advancedText} 

And set up the language "${javascript}"
    Click Element                       ${search_language}
    Input Text                          ${search_language}     ${javascript}
    
And With this many stars "${stars}"
    Click Element                       ${search_stars}
    Input Text                          ${search_stars}        ${stars}
    
And With this license "${license}"
    Scroll Element Into View            ${search_license}
    Click Element                       ${search_license}
    Input Text                          ${search_license}      ${license}

And With this many followers "${followers}"
    Scroll Element Into View            ${search_followers}
    Click Element                       ${search_followers}
    Input Text                          ${search_followers}    ${followers}
    
And hit the search
    Scroll Element Into View            ${advancedSearchText}
    Click Element                       ${advancedSearchText} 

And check if there is only one repository as result
    Wait Until Element Is Visible       ${repositoryResult}

When open the repository
    Click Element                       ${repositoryMvoloskov} 

And open the README
    Click Element                       ${readMe}   

Then the first 300 characters are displayed
    Scroll Element Into View            ${lineCharacters}
