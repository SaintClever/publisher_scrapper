from selenium import webdriver



# Get book links
user_book = input('Book Links: ').replace(',', '').split()


chromedriver = 'chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver)


# MAC user: in Security & Privacy click "Allow Anyway"
# driver.get('https://www.barnesandnoble.com/w/effective-python-brett-slatkin/1130203296?ean=9780134853987')

'''
TEST LINKS: The all have the same number of details / items
https://www.barnesandnoble.com/w/python-crash-course-2nd-edition-eric-matthes/1137572066?ean=9781593279288, https://www.barnesandnoble.com/w/effective-python-brett-slatkin/1130203296?ean=9780134853987, https://www.barnesandnoble.com/w/cracking-codes-with-python-al-sweigart/1126434906?ean=9781593278229
'''

data = []

for book in user_book:
    driver.get(book)

    # product_title = driver.find_elements_by_tag_name('th')
    product_description = driver.find_elements_by_tag_name('td')

    
    # Product Details
    product_details = []
    for i in range(len(product_description)):
        try:
            product_details.append(int(product_description[i].text.replace(',', '')))
        except ValueError:
            product_details.append(product_description[i].text)

    # print(product_details)

    # Product Data
    data.append(tuple(product_details))

print(data)


driver.quit()