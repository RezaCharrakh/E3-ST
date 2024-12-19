from utils import add_item_to_cart, setup, get_num_cart, teardown, get_cart_items, go_to_cart

def test_add_to_cart(driver):
    setup(driver)

    add_item_to_cart(driver, "Espresso")
    add_item_to_cart(driver, "Cappuccino")

    go_to_cart(driver)
    items = get_cart_items(driver)

    assert "Espresso" in items, "Espresso was not added to the cart"
    assert "Cappuccino" in items, "Cappuccino was not added to the cart"


