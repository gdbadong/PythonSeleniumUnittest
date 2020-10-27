from CommonSteps import CommonSteps
import unittest

##### START #####
class Home(unittest.TestCase):
	def test_validationOfProductsDropdownElements(self):
		cs = CommonSteps()
		cs.login()
		cs.validate_products_elements()
		cs.close_browser()

cpd = Home()
cpd.test_validationOfProductsDropdownElements()

if __name__ == '__main__':
	unittest.main()	