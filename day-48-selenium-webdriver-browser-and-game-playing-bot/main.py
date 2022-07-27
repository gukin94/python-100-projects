from selenium import webdriver

chrome_driver_path = "/Users/gukin/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/Fiodio-Mechanical-Keyboards-Anti-Ghosting-Multi-Media/dp/B09NNF3K2C/ref=sr_1_1_sspa?keywords=gaming+keyboard&pd_rd_r=d0db0dc3-d82a-4bc3-b38a-0936871ff803&pd_rd_w=W7nXa&pd_rd_wg=DSRL5&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=TGJ0JJCQQ85D1R6XNTEA&qid=1658847878&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUFpWVlZDUjNRT1ZPJmVuY3J5cHRlZElkPUExMDMwODUzWktTOTVYM1UwQ0pSJmVuY3J5cHRlZEFkSWQ9QTA3MDg1MjQzQVFOTldVV1JGMTlNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
price = driver.find_element_by_class_name("a-offscreen")
print(price)

# driver.close()
driver.quit()