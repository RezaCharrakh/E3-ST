from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def teardown(driver):
    # Close the browser
    driver.quit()
def setup(driver):
    """Initialize the WebDriver and open the Coffee Cart website."""
    driver.get("https://coffee-cart.app/")
    driver.implicitly_wait(1)  # Wait for elements to load
def get_num_cart(driver):
    cart = driver.find_element(By.CSS_SELECTOR, '[aria-label="Cart page"]')
    return cart.text
def add_item_to_cart(driver, item_name):
    """
    Click on a coffee cup to add it to the cart.
    
    :param driver: WebDriver instance
    :param item_name: Name of the coffee (e.g., "Espresso")
    """
    item_selector = f'div[data-test="{item_name}"]'
    cup = driver.find_element(By.CSS_SELECTOR, item_selector)
    cup.click()
    time.sleep(1)  # Wait for the cart to update

def delete_item_from_cart(driver, item_name):
    """
    Deletes a specific item from the cart by clicking its delete button.

    :param driver: WebDriver instance
    :param item_name: The name of the item to delete
    """
    # Find all `li` elements with the class `list-item`
    list_items = driver.find_elements(By.CSS_SELECTOR, "ul > li.list-item")
    
    for item in list_items:
        # Check if the first `div` contains the item name
        name_div = item.find_element(By.CSS_SELECTOR, "div:first-child")
        if name_div.text.strip() == item_name:
            # Find the delete button within the current item and click it
            delete_button = item.find_element(By.CSS_SELECTOR, "button.delete")
            delete_button.click()
            break
    else:
        raise Exception(f"Item '{item_name}' not found in the cart.")


def go_to_cart(driver):
    cart_link = driver.find_element(By.CSS_SELECTOR, '[aria-label="Cart page"]')
    cart_link.click()
    time.sleep(1)  # Wait for the cart page to load

def get_cart_items(driver):
    """
    Get the list of item names in the cart.

    :param driver: WebDriver instance
    :return: List of item names in the cart
    """
    # Find all the `li` elements with the class `list-item`
    list_items = driver.find_elements(By.CSS_SELECTOR, "ul > li.list-item")
    
    # Extract the text from the first `div` inside each list item
    item_names = [item.find_element(By.CSS_SELECTOR, "div:first-child").text for item in list_items]
    
    return item_names
def get_total_price(driver):
    """
    Retrieve the total price from the cart.
    
    :param driver: WebDriver instance
    :return: Total price as a string
    """
    go_to_cart(driver)

    total_price_element = driver.find_element(By.CSS_SELECTOR, '[aria-label="Proceed to checkout"]')
    return total_price_element.text

def add_one_item_in_cart(driver, item_name):
    """
    Increases the quantity of a specific item in the cart by clicking the plus button.

    :param driver: WebDriver instance
    :param item_name: The name of the item to increase quantity
    """
    # Find all `li` elements with the class `list-item`
    list_items = driver.find_elements(By.CSS_SELECTOR, "ul > li.list-item")
    
    for item in list_items:
        # Check if the first `div` contains the item name
        name_div = item.find_element(By.CSS_SELECTOR, "div:first-child")
        if name_div.text.strip() == item_name:
            # Find the plus button in the unit-controller div and click it
            plus_button = item.find_element(By.CSS_SELECTOR, ".unit-controller button[aria-label^='Add one']")
            plus_button.click()
            break
    else:
        raise Exception(f"Item '{item_name}' not found in the cart.")

def remove_one_item_in_cart(driver, item_name):
    """
    Decreases the quantity of a specific item in the cart by clicking the minus button.

    :param driver: WebDriver instance
    :param item_name: The name of the item to decrease quantity
    """
    # Find all `li` elements with the class `list-item`
    list_items = driver.find_elements(By.CSS_SELECTOR, "ul > li.list-item")
    
    for item in list_items:
        # Check if the first `div` contains the item name
        name_div = item.find_element(By.CSS_SELECTOR, "div:first-child")
        if name_div.text.strip() == item_name:
            # Find the minus button in the unit-controller div and click it
            minus_button = item.find_element(By.CSS_SELECTOR, ".unit-controller button[aria-label^='Remove one']")
            minus_button.click()
            break
    else:
        raise Exception(f"Item '{item_name}' not found in the cart.")

def get_item_quantity(driver, item_name):
    """
    Retrieves the quantity of a specific item in the cart.

    :param driver: WebDriver instance
    :param item_name: The name of the item to retrieve quantity
    :return: The quantity of the item as an integer
    """
    # Find all `li` elements with the class `list-item`
    list_items = driver.find_elements(By.CSS_SELECTOR, "ul > li.list-item")
    
    for item in list_items:
        # Check if the first `div` contains the item name
        name_div = item.find_element(By.CSS_SELECTOR, "div:first-child")
        if name_div.text.strip() == item_name:
            # Extract the quantity from the `unit-desc` span
            unit_desc = item.find_element(By.CSS_SELECTOR, ".unit-desc").text
            quantity = int(unit_desc.split('x')[-1].strip())  # Extract the quantity after "x"
            return quantity
    raise Exception(f"Item '{item_name}' not found in the cart.")

def add_items_to_cart(driver, times):
    """
    Add a specific number of items to the cart.

    Args:
        driver: WebDriver instance.
        times: Number of times to add items to the cart.
    """
    for _ in range(times):
        add_item_to_cart(driver, "Espresso")


def check_for_lucky_day_promo(driver):
    """
    Check if the lucky-day promo element is present.

    Returns:
        bool: True if promo is found, False otherwise.
    """
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.promo"))
        )
        return True
    except TimeoutException:
        return False
    

def verify_discounted_mocha_in_cart(driver):
    """
    Verify the discounted Mocha in the cart.

    Returns:
        bool: True if the discounted Mocha is present with correct price and quantity, False otherwise.
    """
    try:
        # Locate the cart items
        cart_items = driver.find_elements(By.CSS_SELECTOR, "ul > li.list-item")
        
        for item in cart_items:
            # Check if the item is the discounted Mocha
            item_name = item.find_element(By.CSS_SELECTOR, "div:first-child").text
            if item_name == "(Discounted) Mocha":
                # Verify the price
                price = item.find_element(By.CSS_SELECTOR, "div:nth-child(3)").text
                if price != "$4.00":
                    return False

                # Verify the quantity
                quantity_desc = item.find_element(By.CSS_SELECTOR, "span.unit-desc").text
                if not quantity_desc.endswith("x 1"):
                    return False

                return True
        return False  # Mocha not found
    except Exception as e:
        print(f"Error verifying discounted Mocha: {e}")
        return False


def handle_lucky_day_promo(driver):
    """
    Handle the lucky-day promo by clicking "Yes" to add the discounted Mocha to the cart.
    """
    try:
        # Locate and click the "Yes" button on the promo
        yes_button = driver.find_element(By.CSS_SELECTOR, "div.promo button.yes")
        yes_button.click()

        # Wait for confirmation that the promo is handled (e.g., promo disappears or cart updates)
        WebDriverWait(driver, 2).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.promo"))
        )
    except Exception as e:
        print(f"Error handling lucky-day promo: {e}")

def attempt_increase_discounted_mocha_quantity(driver):
    """
    Attempt to increase the quantity of the discounted Mocha in the cart and ensure it remains at 1.
    Returns True if quantity does not increase, otherwise False.
    """
    try:
        cart_items = driver.find_elements(By.CSS_SELECTOR, "ul > li.list-item")
        for item in cart_items:
            item_name = item.find_element(By.CSS_SELECTOR, "div:first-child").text
            if item_name == "(Discounted) Mocha":
                # Find and click the "+" button
                plus_button = item.find_element(By.CSS_SELECTOR, "button[aria-label*='Add one']")
                plus_button.click()

                # Wait for the cart to update
                WebDriverWait(driver, 2).until(
                    EC.text_to_be_present_in_element(
                        (By.CSS_SELECTOR, "span.unit-desc"), "$4.00 x 1"
                    )
                )

                # Verify the quantity description
                quantity_desc = item.find_element(By.CSS_SELECTOR, "span.unit-desc").text
                return quantity_desc.endswith("x 1")  # Returns True if quantity is still 1
        return False
    except Exception as e:
        raise AssertionError(f"Error attempting to increase quantity for discounted Mocha: {e}")

def open_payment_details_modal(driver):
    """
    Click the total button to open the Payment Details modal.
    """
    try:
        total_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Proceed to checkout"]')
        total_button.click()

        # Wait for the modal to appear
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-content"))
        )
    except Exception as e:
        raise AssertionError(f"Error opening Payment Details modal: {e}")
    
def fill_email_payment_form(driver, name, email, agree_to_promotions=False):
    """
    Fill in the payment form with the provided details.

    Args:
        driver: The WebDriver instance.
        name: The name to input.
        email: The email to input.
        agree_to_promotions: Whether to check the promotions checkbox.
    """
    # Fill in the name and email
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)

    # Check the promotions checkbox if required
    if agree_to_promotions:
        promotion_checkbox = driver.find_element(By.ID, "promotion")
        promotion_checkbox.click()

def is_modal_visible(driver):
    """
    Check if the modal is still visible on the page.
    """
    return driver.find_element(By.CLASS_NAME, "modal").is_displayed()
    
def verify_success_message(driver, success_text="Payment link sent", timeout=5):
    """
    Wait for the success message to appear and verify its content.
    
    Args:
        driver: The WebDriver instance.
        success_text: The text to verify in the success message.
        timeout: The maximum time to wait for the success message.

    Raises:
        AssertionError: If the success message is not found or does not contain the expected text.
    """
    try:
        success_message = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
        )
        assert success_text in success_message.text, f"Expected success message '{success_text}' not found."
    except Exception as e:
        raise AssertionError(f"Failed to verify success message: {e}")