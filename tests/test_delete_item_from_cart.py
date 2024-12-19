from utils import add_item_to_cart, go_to_cart, get_cart_items, setup, delete_item_from_cart

def test_delete_item_from_cart(driver):
    setup(driver)

    add_item_to_cart(driver, "Espresso")
    add_item_to_cart(driver, "Cappuccino")

    go_to_cart(driver)

    delete_item_from_cart(driver, "Espresso")

    items = get_cart_items(driver)

    assert "Espresso" not in items, "Espresso was not deleted"
    assert "Cappuccino" in items, "Espresso Macchiato is missing from the cart"
