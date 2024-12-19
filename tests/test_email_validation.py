from selenium.webdriver.common.by import By
from utils import setup, open_payment_details_modal, fill_email_payment_form, is_modal_visible


def test_email_validation(driver):
    setup(driver)
    open_payment_details_modal(driver)

    # Fill the form with invalid email
    fill_email_payment_form(driver, name="Test User", email="invalid-email")

    # Submit the form
    driver.find_element(By.ID, "submit-payment").click()

    # Verify that modal is still visible
    assert is_modal_visible(driver), "Modal should remain visible for invalid email."
    print("Email validation test passed.")