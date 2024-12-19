from utils import add_item_to_cart, setup, get_total_price, teardown
def test_total_price(driver):
    setup(driver)

    add_item_to_cart(driver, "Espresso")
    add_item_to_cart(driver, "Cappuccino")

    total_price = get_total_price(driver)
    assert total_price == "Total: $29.00", f"Expected $29.00 but got {total_price}"

