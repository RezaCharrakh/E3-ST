from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import open_payment_details_modal, setup, fill_email_payment_form

def test_successful_email_submission(driver):
    setup(driver)
    open_payment_details_modal(driver)

    # Fill the form with valid details
    fill_email_payment_form(driver, name="Test User", email="test@example.com", agree_to_promotions=True)

    # Submit the form
    driver.find_element(By.ID, "submit-payment").click()

    # Wait for the success message to appear
    success_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbar.success"))
    )

    # Assert that the success message text is correct
    assert success_message.text == "Thanks for your purchase. Please check your email for payment.", \
        "Success message did not match expected text."

    print("Successful email submission test passed.")