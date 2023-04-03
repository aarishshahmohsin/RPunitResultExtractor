from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Firefox()


# print(driver.title)

with open('all data.csv') as file_obj:

    reader_obj = csv.reader(file_obj)
    i = 0
    for row in reader_obj:
        if i != 20:
        
            driver.get("https://ctengg.amu.ac.in/web/st_result001.php?prog=btech")
            fac_no = '//*[@id="facno_input"]'
            enrol_no = '//*[@id="eno_input"]'
            submit_button = '//*[@id="att_submit"]'

            s1 = row[1]
            s2 = row[0]

            driver.find_element(By.XPATH, fac_no).send_keys(s2)
            # faculty = driver.find_element(By.XPATH, fac_no)

            driver.find_element(By.XPATH, enrol_no).send_keys(s1)
            driver.find_element(By.XPATH, submit_button).click()

            # driver.save_screenshot('./noe{}.png'.format(i+1))
            elements = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[6]')
            content = elements.text
            # for i in range(1, 11):
            #     print(i)
            # content = "".join([element.text for element in elements])
            print(s2, ", ", content)
        i += 1



        
driver.quit()