from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

import time
import unittest
import HtmlTestRunner

class Home(unittest.TestCase):
	# binary = r'C:/Users/glenn.d.badong/AppData/Local/Mozilla Firefox/firefox.exe'
	# options = Options()
	# options.set_headless(headless=True)
	# options.binary = binary
	# cap = DesiredCapabilities().FIREFOX
	# cap["marionette"] = False
	# driver = webdriver.Firefox(capabilities=cap, executable_path = 'C:/Users/glenn.d.badong/Documents/WORK/Clockwork/ArcadisGen_Automation/geckodriver.exe')

	driver = webdriver.Chrome(executable_path = 'C:/Users/glenn.d.badong/Documents/WORK/Clockwork/ArcadisGen_Automation/chromedriver.exe')
	
	wait = WebDriverWait(driver, 20)
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


	#######################################################
	#################### START OF TEST ####################
	#######################################################
	def test_checkingHomeButtonsAndTexts(self):
		driver = self.driver

		"""this will open url in browser"""
		self.open_url()

		"""this will validate all header buttons"""
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Products')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'PROJECTS')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'INSIGHTS')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'What We Do')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Who We Are')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Join Us')]")
		
		"""this will validate all elements under products dropdown"""
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Products')]").click()
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Enterprise Decision Analytics')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Enterprise Asset Management')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'InvestSmart')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Universal Visual Optimizer')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Water Above Ground Optimizer')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Water AI Pipe Predictor')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Omnia')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'VIEW ALL PRODUCTS')]")
		
		"""this will validate all elements under 'what we do' dropdown"""
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'What We Do')]").click()
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Rail')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Aviation')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Highways & Road Fleet')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Energy')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Water')]")
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'Buildings')]")
		driver.find_element_by_xpath("//*[contains(text(), 'MORE ABOUT WHAT WE DO')]")

		driver.find_element_by_class_name('scroll-spy__list')
		driver.find_element_by_id('slick-slide-control01')

		"""this will validate buttons all across the page"""
		driver.find_element_by_xpath("//*/button[@class='slick-prev slick-arrow']")
		# print("'previous' button background-color %s"%driver.find_element_by_xpath("//*/button[@class='slick-prev slick-arrow']").value_of_css_property("background-color"))
		# print("'previous' button color %s"%driver.find_element_by_xpath("//*/button[@class='slick-prev slick-arrow']").value_of_css_property("color"))
		driver.find_element_by_xpath("//*/button[@class='slick-next slick-arrow']")
		# print("'next' button background-color %s"%driver.find_element_by_xpath("//*/button[@class='slick-next slick-arrow']").value_of_css_property("background-color"))
		# print("'next' button color %s"%driver.find_element_by_xpath("//*/button[@class='slick-next slick-arrow']").value_of_css_property("color"))
		driver.find_element_by_xpath("//*[contains(text(), 'Find out more')]")
		# print("'find out more' button background-color %s"%driver.find_element_by_xpath("//*[contains(text(), 'Find out more')]").value_of_css_property("background-color"))
		# print("'find out more' button color %s"%driver.find_element_by_xpath("//*[contains(text(), 'Find out more')]").value_of_css_property("color"))
		driver.find_element_by_xpath("//*[contains(text(), 'Contact us')]")
		# print("'contact us' button background-color %s"%driver.find_element_by_xpath("//*[contains(text(), 'Contact us')]").value_of_css_property("background-color"))
		# print("'contact us' button color %s"%driver.find_element_by_xpath("//*[contains(text(), 'Contact us')]").value_of_css_property("color"))

		self.scrolldown_until_inview("//*/div/a[contains(text(), 'DISCOVER WHO WE ARE')]")
		# element = driver.find_element_by_xpath("//*/div/a[contains(text(), 'DISCOVER WHO WE ARE')]")
		# driver.execute_script("arguments[0].scrollIntoView(true);", element)
		# print("'discover who we are' button background-color %s"%driver.find_element_by_xpath("//*[contains(text(), 'DISCOVER WHO WE ARE')]").value_of_css_property("background-color"))
		# print("'discover who we are' button color %s"%driver.find_element_by_xpath("//*[contains(text(), 'DISCOVER WHO WE ARE')]").value_of_css_property("color"))
		driver.find_element_by_xpath("//*/div/h1[contains(text(), 'Generate')]")
		# driver.find_element_by_xpath("//*/div/h1[contains(text(), 's next')]")
		# driver.find_element_by_xpath("//*[contains(text(), Bold, disruptive, experimental - the pioneers of what')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Across the built and natural environment, we empower the businesses that make the world go round.')]")
		# time.sleep(0.5)

		self.scrolldown_until_inview("//*/div/a[contains(text(), 'DISCOVER WHO WE ARE')]")
		# element = driver.find_element_by_xpath("//*/div/a[contains(text(), 'DISCOVER WHO WE ARE')]")
		# driver.execute_script("arguments[0].scrollIntoView(true);", element)
		driver.find_element_by_xpath("//*[contains(text(), 'Unleash the potential of your data')]")
		
		self.scrolldown_until_inview("//*[@id='content']/div[1]/div/div[4]/div/div[2]/div/div/a")
		# element = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[2]/div/div/a")
		# driver.execute_script("arguments[0].scrollIntoView(true);", element)
		driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[3]/div/div/a")
		driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[4]/div/div/a")
		driver.find_element_by_xpath("//*[contains(text(), 'Plan')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Deliver')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Operate & Maintain')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Optimize expenditure for sustainable returns. Asset investment planning and decision support analytics tools to help you make better informed, data-driven decisions.')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Enhance the performance of your investment programs. Manage cost and risk for seamless delivery. Program management and cost control solutions that put you in complete control.')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Improve asset reliability and availability. A game-changing combination of enterprise asset management solutions and advanced analytics to help you maintain operational efficiency, and plan with confidence.')]")
		
		self.scrolldown_until_inview("//*[@id='content']/div[1]/div/div[5]/div/div[2]/div/a")
		# element = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[5]/div/div[2]/div/a")
		# driver.execute_script("arguments[0].scrollIntoView(true);", element)
		driver.find_element_by_xpath("//*[contains(text(), 'How can we help?')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Exploring?')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Rail')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Aviation')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Highways & Road Fleet')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Energy')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Water')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Buildings')]")

		self.scrolldown_until_inview("//*[@id='content']/div[1]/div/div[6]/div/div/div/div/div[2]/div/a")
		# element = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[6]/div/div/div/div/div[2]/div/a")
		# driver.execute_script("arguments[0].scrollIntoView(true);", element)
		driver.find_element_by_xpath("//*[contains(text(), 'Featured Projects')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Transport for London, United Kingdom')]")
		driver.find_element_by_xpath("//*[contains(text(), 'Improving passenger journeys across London')]")

		self.assertTrue(True)


	def test_validateProjects(self):
		driver = self.driver
		self.frame_switch()
		driver.find_element_by_xpath("//*/div/a[contains(text(), 'PROJECTS')]").click()
		driver.find_element_by_xpath("//*[contains(text(), 'Projects')]")
		driver.find_element_by_xpath("//*[contains(text(), 'See how Arcadis Gen has helped transform performance for organizations around the world')]")

		self.assertTrue(True)

		"""close the website"""
		self.close_browser()



if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner
		# .HTMLTestRunner(output='C:/Users/glenn.d.badong/Documents/WORK/Clockwork/ArcadisGen_Automation/report',
		.HTMLTestRunner(output='../report',
			report_title='Sample ArcadisGen_Automation Test'))