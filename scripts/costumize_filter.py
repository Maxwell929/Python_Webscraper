from scripts.setup import driver, find_Elements, collection

id = 0


def filtering():
    # refresh cause selenium gives this answer:  stale element reference: element is not attached to the page document
    driver.refresh()

    job = find_Elements('//a[@class="m-jobsListItem__titleLink"]')
    company = find_Elements("//a[@class='m-jobsListItem__companyName m-jobsListItem__companyName--link']")
    date = find_Elements("//span[@class='m-jobsListItem__date']")
    description = find_Elements("//p[@class='m-jobsListItem__snippet']")
    link = find_Elements('//a[@class="m-jobsListItem__titleLink"]')

    # iterating all the elements into a dictionary and storing them into a the list from the search file
    for j, c, d, de, li in zip(job, company, date, description, link):
        global id
        id += 1

        data = {
            "id": id,
            "Job": j.text,
            "Unternehmen": c.text,
            "Datum": d.text.replace("am ", ""),
            "Beschreibung": de.text,
            "Link": li.get_attribute("href")
        }
        print(id)
        collection.insert(data)
