*** settings ***
Resource    ../variables/global_var.robot

Library    ../libraries/Selenium_Wrapper.py
Library    ../libraries/userdef_keywords.py
*** Variables ***
${product_name}    Sauce Labs Backpack
${product_xpath}    //div[text()='${product_name}']/ancestor::div[@class='inventory_item']//button[text() = 'Add to cart']
@{productnames}    Sauce Labs Backpack    Sauce Labs Bike Light


*** Keywords ***

Add Product
    Click    xpath    ${product_xpath}    Add product to cart

Click Cart
    Click    class    shopping_cart_link    Shopping Cart

Verify Cart
    Find Element    xpath    //div[@class = 'cart_item_label']//div[text() = '${product_name}']

Add Multiple Products
    FOR    ${product}    IN    @{productnames}
        ${product_xpath}=    Set Variable    xpath=//div[text()='${product}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart]'
        Click    xpath    ${product_xpath}    Add products to cart
    END
    Click    class    shopping_cart_link    Shopping Cart
    Click    id    checkout    Move to Checkout

Fill Checkout Info
    Enter Text    id    first-name    Standard    First Name
    Enter Text    id    last-name    User    Last Name
    Enter Text    id    postal-code    211412    Zip
    Click    id    continue    Click Continue

Verify Items
    FOR    ${product}    IN    @{productnames}
        Find Element    xpath    //div[@class='inventory_item_name' and text()='${product}']
    END

Check Quantity
    Find Element    xpath    //div[@class='cart_quantity' and text()='1']
