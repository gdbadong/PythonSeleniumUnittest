from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class CommonSteps:
	
	driver = webdriver.Chrome(executable_path = 'C:/Users/glenn.d.badong/Documents/WORK/Clockwork/ArcadisGen_Automation/chromedriver.exe')
	
	wait = WebDriverWait(driver, 10)
	url = "https://www.arcadisgen.com/"
	driver.implicitly_wait(10)

	"""this will open URL in browser"""
	def open_url(self):
		self.driver.get(self.url)
		self.driver.maximize_window()

		"""click accept"""
		self.wait_until_xpath_exists("//*[@id='cookiebot-js']/div/div[2]/div[3]/a[1]")
		try:
		    self.driver.find_element_by_xpath("//*[@id='cookiebot-js']/div/div[2]/div[3]/a[1]").click()
		except NoSuchElementException:
		    print("cookiebot not found")

	"""this will close browser"""
	def close_browser(self):
		self.driver.close()

	"""this will swith to main / default iframe"""
	def frame_switch(self):
		self.driver.switch_to.default_content()

	# """
	# this will wait until xpath element is visible:
	# STEP:
	# 	wait_until_xpath_exists(expat)
	# WHEREAS:
	# 	wait_until_xpath_exists(<xpath of element>)
	# 	expat = xpath of the element being searched
	# """
	def wait_until_xpath_exists(self, expat):
		self.wait.until(ec.presence_of_element_located((By.XPATH, expat)))

	# """
	# this will scroll down until element is in view:
	# STEP:
	# 	scrolldown_until_inview(expat)
	# WHEREAS:
	# 	scrolldown_until_inview(<xpath of element>)
	# 	expat = xpath of the element being searched
	# """
	def scrolldown_until_inview(self, expat):
		element = self.driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[6]/div/div/div/div/div[2]/div/a")
		self.driver.execute_script("arguments[0].scrollIntoView(true);", element)