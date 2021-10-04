**Settings**
Library    ../lib/CustomLib.py
Library     OperatingSystem
Resource    page_objects.robot
Resource    keywords.robot
Library     RequestsLibrary
Library     Collections

**Variables**
${url_github}      https://github.com 

***Keywords***

Open Session
    Open Browser            ${url_github}      chrome
    Maximize Browser Window
    Login in publisher

Close Session
    Capture Page Screenshot
    Close Browser