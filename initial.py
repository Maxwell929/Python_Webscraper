from scripts.setup import driver
from scripts.search_costumization import initialization
from scripts.costumize_filter import filtering, sammlung
from scripts.new_site import next_Site
import json


# Filters the actuall site and goes then to the next site
def filtering_Sites():
	filtering()
	next_Site()


# function to start  the scrapper
def init():
	initialization()
	filtering_Sites()


# Starts the scrapper
init()

# Filter the next Page(s)
# Page 2
filtering_Sites()
# Page 3
filtering_Sites()


# Save all the filtered jobs into a JSON file
with open('JSON/Liste_Stellen.json', 'w') as fp:
	json.dump(sammlung, fp, indent=4, )

# closing process
driver.quit()
