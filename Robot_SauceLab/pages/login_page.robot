*** settings ***
Resource    ../variables/global_var.robot

Library    ../libraries/Selenium_Wrapper.py
Library    ../libraries/userdef_keywords.py

*** Variables ***

${signin_button_xpath}     (//a[@aria-label='Open the Sign into Gmail page in a new tab']//span[text()='Sign in'])[2]
${emailid_text_box_xpath}    //div[text()='Email or phone']/preceding-sibling::input
@{usernames}    karthi    boopalan    Vidhya    Thavamani
&{userdetails}    name=Akshay    email=akshay@gmail.com    mobile=738374833
*** Keywords ***

Enter User Credentials


    IF    '${flag}' == 'POSITIVE'
        Enter Text    id    user-name    ${userid}            username
        Enter Text    id    password     ${pwd}               password
    ELSE IF    '${flag}' == 'NEGATIVE'
        Enter Text    id    user-name    ${invalid_userid}    username
        Enter Text    id    password     ${invalid_pwd}       password
    ELSE
        Fail    Invalid flag provided: ${flag}
    END

Click On Login Button
    Click    id    login-button    login button


