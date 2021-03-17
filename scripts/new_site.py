from scripts.setup import find_Element
import time

def next_Site():
	next_button = find_Element('//button[@data-event-action="click: pagination-next"]')
	next_button.location_once_scrolled_into_view
	next_button.click()
	time.sleep(1)