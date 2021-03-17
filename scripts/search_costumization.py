import time
from scripts.setup import find_Element, website

#start the website
website


# Function where I select the Element for my search
# time.sleep is for the loading time, cause somtimes the site is loading verey slow(bad internet) and selenium isn't able to find the elements'
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
	time.sleep(0.5)

	# Selecting Berufsfelder
	target = find_Element('//strong[contains(text(), "Berufsfelder")]')
	target.click()
	time.sleep(0.7)

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

	time.sleep(0.5)
	
	# of cours all this can be costumized
