
from scripts.setup import find_Element, driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 10
w = WebDriverWait(driver, timeout)
prs = EC.presence_of_element_located



# Function where I select the Element for my search
# time.sleep is for the loading time, cause sometimes the site is loading and selenium isn't able to find the elements'
def initialization():
	# Input Beruf and area
	input_beruf = find_Element('//input[@placeholder="Beruf, Begriff"]')
	input_beruf.send_keys("IT")

	input_area = find_Element('//input[@name="locations"]')
	input_area.send_keys("Wien")

	# Close cookie window
	cookie = find_Element('//button[@class="k-blockingCookieModal__button k-blockingCookieModal__button--karriere"]')
	cookie.click()

	# Submit the Search
	target = find_Element('//button[@type="submit"]')
	target.click()


	# Selecting Berufsfelder

	#Waits until the element is visible in the DOM. Replaces the time.sleep() function. So wheather you have a fast or slower internet it will always wait until it has loaded
	w.until(prs((By.XPATH, '//strong[contains(text(), "Berufsfelder")]')))


	target = find_Element('//strong[contains(text(), "Berufsfelder")]')
	target.click()

	w.until(prs((By.XPATH, '//span[contains(text(), "IT, EDV")]')))

	target = find_Element('//span[contains(text(), "IT, EDV")]')
	target.click()


	# Select Positionsebene
	target = find_Element('//strong[contains(text(), "Positionsebene")]')
	target.click()

	target = find_Element('//span[contains(text(), "Einsteiger")]')
	target.click()

	# click finden button

	target = find_Element('//button[contains(text(), "Jobs finden")]')
	target.click()

	w.until(prs((By.XPATH, '//li[@class="m-jobsFilterButtons__tag"]')))

