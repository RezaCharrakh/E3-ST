from utils import go_to_cart, setup, add_items_to_cart, check_for_lucky_day_promo, handle_lucky_day_promo, verify_discounted_mocha_in_cart, attempt_increase_discounted_mocha_quantity


def test_lucky_day_discounted_mocha(driver):
    setup(driver)
    """
    Test to ensure the lucky-day discounted Mocha promotion works correctly when it appears after 3 additions.
    """
    # Step 1: Add coffee to cart until lucky-day promo appears
    add_items_to_cart(driver, times=3)
    assert check_for_lucky_day_promo(driver), "Lucky-day promo did not appear after 3 additions."

    # Step 2: Accept the lucky-day promo
    handle_lucky_day_promo(driver)
    go_to_cart(driver)

    # Step 3: Verify discounted Mocha is correctly added to the cart
    assert verify_discounted_mocha_in_cart(driver), "Discounted Mocha quantity or price is incorrect."

    # Step 4: Attempt to increase the quantity of the discounted Mocha
    assert attempt_increase_discounted_mocha_quantity(driver), "Discounted Mocha quantity increased, which is incorrect."

    print("Test passed: (Discounted) Mocha quantity is restricted to 1.")
