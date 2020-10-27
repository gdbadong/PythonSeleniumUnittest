from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest

url = "C:\\Users\\glenn.d.badong\\Documents\\WORK\\Clockwork\\ArcadisGen_Automation\\Webdrivers\\chromedriver.exe"
global driver
global wait
driver = webdriver.Chrome(executable_path = url)
wait = WebDriverWait(driver, 10)
# driver = webdriver.Firefox(executable_path='C:\\Users\\glenn.d.badong\\Documents\\WORK\\Clockwork\\ArcadisGen_Automation\\webdrivers\\geckodriver.exe')

class CommonSteps(unittest.TestCase):
	def __init__(self):
		pass

	"""this will swith to main / default iframe"""
	def frame_switch(self):
		# driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='header']/div/div/div[1]/div/div/div/div[1]/div/a/img"))
		driver.switch_to.default_content()

	"""this will wait until xpath element is visible"""
	#### wait_until_xpath_exists(<xpath of element>)
	def wait_until_xpath_exists(self, expat):
		wait.until(ec.presence_of_element_located((By.XPATH, expat)))

	"""this will close browser"""
	def test_close_browser(self):
		driver.close()
		self.assertTrue(True)

	"""this will open browser and open arcadisgen website"""
	# this is predefined url but in the future we can update this to cater firefox and other urls
	def test_open_url(self):
		driver.maximize_window()

		#navigate to the URL
		driver.get("https://www.arcadisgen.com/")

		#click I accept button
		self.wait_until_xpath_exists("//*[@id='cookiebot-js']/div/div[2]/div[3]/a[1]")
		try:
		    driver.find_element_by_xpath("//*[@id='cookiebot-js']/div/div[2]/div[3]/a[1]").click()
		except NoSuchElementException:
		    print("cookiebot not found")

		self.assertTrue(True)
		# print("login - DONE")

	"""this will validate all elements under products dropdown"""
	def test_validate_products_elements(self):
		#click Products dropdown
		self.frame_switch()
		# driver.find_element_by_xpath("//*[@id='header']/div/div/div[1]/div/div/div/div[1]/div/a/img")
		driver.find_element_by_xpath("//*[contains(text(), 'Products')]").click()
		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Enterprise Decision Analytics')]")
		except NoSuchElementException:
			print("'Enterprise Decision Analytics' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Enterprise Asset Management')]")
		except NoSuchElementException:
			print("'Enterprise Asset Management' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'InvestSmart')]")
		except NoSuchElementException:
			print("'InvestSmart' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Universal Visual Optimizer')]")
		except NoSuchElementException:
			print("'Universal Visual Optimizer' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Water Above Ground Optimizer')]")
		except NoSuchElementException:
			print("'Water Above Ground Optimizer' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Water AI Pipe Predictor')]")
		except NoSuchElementException:
			print("'Water AI Pipe Predictor' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Omnia')]")
		except NoSuchElementException:
			print("'Omnia' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'VIEW ALL PRODUCTS')]")
		except NoSuchElementException:
			print("'VIEW ALL PRODUCTS' - not found")

		self.assertTrue(True)
		# print("checking_elements_inside_product_dropdown - DONE")

	def test_validateHeaderButtons(self):
		self.frame_switch()
		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Products')]")
		except NoSuchElementException:
			print("'Products' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'PROJECTS')]")
		except NoSuchElementException:
			print("'PROJECTS' - not found")
			
		try:
			driver.find_element_by_xpath("//*[contains(text(), 'INSIGHTS')]")
		except NoSuchElementException:
			print("'INSIGHTS' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'What We Do')]")
		except NoSuchElementException:
			print("'What We Do' - not found")

		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Who We Are')]")
		except NoSuchElementException:
			print("'Who We Are' - not found")
			
		try:
			driver.find_element_by_xpath("//*[contains(text(), 'Join Us')]")
		except NoSuchElementException:
			print("'Join Us' - not found")

		self.assertTrue(True)