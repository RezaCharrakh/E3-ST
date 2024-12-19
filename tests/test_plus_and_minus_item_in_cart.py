from utils import add_item_to_cart, go_to_cart, get_item_quantity, add_one_item_in_cart, remove_one_item_in_cart, setup

def test_plus_and_minus_item_in_cart(driver):
    setup(driver)
    # Add an item to the cart
    add_item_to_cart(driver, "Espresso")
    go_to_cart(driver)
    
    # Check initial quantity
    initial_quantity = get_item_quantity(driver, "Espresso")
    assert initial_quantity == 1, "Initial quantity should be 1"
    
    # Add one more item
    add_one_item_in_cart(driver, "Espresso")
    updated_quantity = get_item_quantity(driver, "Espresso")
    assert updated_quantity == 2, "Quantity should increase to 2"
    
    # Remove one item
    remove_one_item_in_cart(driver, "Espresso")
    reduced_quantity = get_item_quantity(driver, "Espresso")
    assert reduced_quantity == 1, "Quantity should decrease back to 1"
