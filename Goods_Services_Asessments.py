from lib2to3.pgen2 import driver
from select import select
import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class TestGoodsServicesAsessments(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_goods_services_asessments_add(self):
        driver=self.driver
        driver.maximize_window()
        driver.get("http://10.9.98.65/gais65/")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/input[4]").send_keys("it.appsupport")
        time.sleep(1)
        driver.find_element(By.ID,"regularInput").send_keys("Gais432")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/div/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@id='14']").click()
        time.sleep(3)
        driver.find_element(By.ID,"save").click()
        time.sleep(5)

        driver.find_element(By.XPATH,"//a[@data-id='427']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//*[@id='icons']/ul/li/a[2]/img").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[2]/img").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[1]/img").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//[@title='Add Vendor Evaluation Goods / Services']").click()
        time.sleep(1)

        # select=Select(driver.find_element(By.ID,"search_po_number"))
        # select.select_by_visible_text()

        nopo = driver.find_element(By.ID,"search_po_number")
        nopo.send_keys("PO01430087")
        time.sleep(1)
        role.send_keys(Keys.ARROW_DOWN)
        role.send_keys(Keys.ENTER)
        time.sleep(1)
        select=Select(driver.find_element(By.ID,"assesment_type"))
        select.select_by_visible_text("Goods")
        driver.find_element(By.XPATH,"//*[@id='list_po_details']/tr[2]/td[1]/input").click()
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[1]/div/button").click()
        time.sleep(1)

        # select=Select(driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[2]/div[1]/table/tbody/tr[1]/td[4]/select"))
        # select.select_by_visible_text("")
        select=Select(driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[2]/div[1]/table/tbody/tr[2]/td[4]/select"))
        select.select_by_visible_text("A")
        select=Select(driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[2]/div[1]/table/tbody/tr[3]/td[4]/select"))
        select.select_by_visible_text("A")
        select=Select(driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[2]/div[1]/table/tbody/tr[4]/td[4]/select"))
        select.select_by_visible_text("A")
        select=Select(driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[2]/div[1]/table/tbody/tr[5]/td[4]/select"))
        select.select_by_visible_text("B")
        select=Select(driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[2]/div[1]/table/tbody/tr[6]/td[4]/select"))
        select.select_by_visible_text("B")

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div/div[2]/div[4]/button").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("PO01430087")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[2]/td/button").click()
        time.sleep(2)




    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()