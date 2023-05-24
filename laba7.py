


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver (e.g., ChromeDriver)

# Open the Steam page
driver.get("https://store.steampowered.com/")

# Test 1: Check the presence of the Steam logo
logo = driver.find_element("css selector",".mainmenu_footer_logo")
assert logo.is_displayed()

# Test 2: Search for games
search_box = driver.find_element_by_name("term")
search_box.send_keys("The Witcher 3")
search_box.send_keys(Keys.RETURN)
time.sleep(2)  # Wait for 2 seconds for the results to load

# Check the presence of search results
search_results = driver.find_elements_by_class_name("search_result_row")
assert len(search_results) > 0

# Test 3: Add a game to the wishlist
first_result = search_results[0]
add_to_wishlist_button = first_result.find_element_by_css_selector(".wishlist_add_to_wishlist")
add_to_wishlist_button.click()
time.sleep(2)  # Wait for 2 seconds to add the game to the wishlist

# Check that the game was successfully added to the wishlist
wishlist_link = driver.find_element_by_css_selector(".user_wishlist_stats a")
wishlist_count = wishlist_link.text
assert wishlist_count == "1"

# Close the browser
driver.quit()
