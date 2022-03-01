class Field:
    username_textfield = "//input[@id='user-name']"
    username_passwordfield = "//input[@id='password']"
    login_button = "//input[@id='login-button']"

    product_span = "//span[@class= 'title']"
    product_sort = "//select[@class='product_sort_container']"
    select_by_value = "//option[@value='hilo']"

    add_to_cart = "//button[@ id = 'add-to-cart-sauce-labs-backpack']"
    add_to_cart_1 = "//button[@ id = 'add-to-cart-sauce-labs-bike-light']"
    add_to_cart_2 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"

    inside_the_cart = "//div[@id='shopping_cart_container']"
    checkout = "//button[@id='checkout']"
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    click_continue = "//input[@id='continue']"
    total = "//div[@class='summary_total_label']"
    sub_total = "//div[@class='summary_subtotal_label']"
    get_tax = "//div[@class='summary_tax_label']"
