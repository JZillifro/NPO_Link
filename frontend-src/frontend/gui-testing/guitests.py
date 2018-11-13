from sys import platform
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AcceptanceTests (TestCase):

	def setUp(self):
		self.homeurl = 'http://localhost'
		if platform == "linux" or platform == "linux2":
			self.browser = webdriver.Chrome('./chrome_drivers/chromedriver_linux')
		elif platform == "darwin": # macOS
			self.browser = webdriver.Chrome('./chrome_drivers/chromedriver_macosx')
		elif platform == "win32":
			self.browser = webdriver.Chrome('./chrome_drivers/chromedriver.exe')
		self.browser.get(self.homeurl)

	# # Tests that the browser title for the homepage is correct
	# def test1(self):
	# 	self.browser.get(self.homeurl)
	# 	self.assertIn('NPOLink', self.browser.title)
	#
	# # Tests that the home page component on navigation bar works
	# def test2(self):
	# 	try:
	# 		self.browser.find_element_by_link_text('Home').click()
	# 		self.assertEqual("http://npolink.me/", self.browser.current_url)
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests that the homepage header is correct
	# def test3(self):
	# 	self.browser.find_element_by_link_text('Home').click()
	# 	given = self.browser.find_element_by_class_name("inner").text
	# 	self.assertIn('NPOLink', given)
	#
	# # Tests that nonprofits component on navigation bar works
	# def test4(self):
	# 	try:
	# 		self.browser.find_element_by_link_text('Nonprofits').click()
	# 		self.assertEqual("http://npolink.me/nonprofits", self.browser.current_url)
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests that the nonprofits header is correct
	# def test5(self):
	# 	self.browser.find_element_by_link_text('Nonprofits').click()
	# 	given = self.browser.find_element_by_class_name("container").text
	# 	self.assertIn('Nonprofits', given)
	#
	# # Tests that categories component on navigation bar works
	# def test6(self):
	# 	try:
	# 		self.browser.find_element_by_link_text('Categories').click()
	# 		self.assertEqual("http://npolink.me/categories", self.browser.current_url)
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests that the categories header is correct
	# def test7(self):
	# 	self.browser.find_element_by_link_text('Categories').click()
	# 	given = self.browser.find_element_by_class_name("container").text
	# 	self.assertIn('Categories', given)
	#
	# # Tests that locations component on navigation bar works
	# def test8(self):
	# 	try:
	# 		self.browser.find_element_by_link_text('Locations').click()
	# 		self.assertEqual("http://npolink.me/locations", self.browser.current_url)
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests that the locations header is correct
	# def test9(self):
	# 	self.browser.find_element_by_link_text('Locations').click()
	# 	given = self.browser.find_element_by_class_name("container").text
	# 	self.assertIn('Locations', given)
	#
	# # Tests that about component on navigation bar works
	# def test10(self):
	# 	try:
	# 		self.browser.find_element_by_link_text('About').click()
	# 		self.assertEqual("http://npolink.me/about", self.browser.current_url)
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests that the about header is correct
	# def test11(self):
	# 	self.browser.find_element_by_link_text('About').click()
	# 	given = self.browser.find_element_by_class_name("container").text
	# 	self.assertIn('About', given)
	#
	# # Tests that link to gitlab repository works
	# def test12(self):
	# 	self.browser.find_element_by_link_text('About').click()
	# 	try:
	# 		self.browser.find_element_by_link_text('GitLab Repository').click()
	# 		self.assertEqual("https://gitlab.com/gerardomares/npolink", self.browser.current_url)
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests added for Phase 3
	#
	# # Make sure can get to universal search page
	# def test14(self):
	# 	try:
	# 		self.browser.find_element_by_link_text('Search').click()
	# 		self.assertEqual("http://npolink.me/all/search", self.browser.current_url)
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# Tests the overall search for the site
	def test13(self):
		# self.browser.find_element_by_link_text('Search').click()

		search_field = self.browser.find_element_by_id("search_bar") # update word "keywords" once implemented
		search_field.click()
		search_field.send_keys("water")

		# might need a time/sleep here
		search_button = self.browser.find_element_by_id("submit_button") # update word "keywords" once implemented
		search_button.click()

		# might need a time/sleep here
		try:
			self.browser.find_element_by_link_text('Pollution Abatement & Control').click() # update word "keywords" once implemented
			self.assertEqual("http://localhost/category/83", self.browser.current_url) # update expected url once implemented
		except NoSuchElementException:
			self.fail("The element doesn't exist")

	# # Tests the search for the Nonprofits page
	# def test14(self):
	# 	self.browser.find_element_by_link_text('Nonprofits').click()
	#
	# 	search_field = self.browser.find_element_by_id("search_bar") # update word "keywords" once implemented
	# 	search_field.click()
	# 	search_field.send_keys("") # send in some type of wording
	#
	# 	# might need a time/sleep here
	# 	search_button = self.browser.find_element_by_id("submit_button") # update word "keywords" once implemented
	# 	search_buttom.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text('Nonprofit Name').click() # update word "keywords" once implemented
	# 		self.assertEqual("http://npolink.me/nonprofit/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the filtering for the Nonprofits page
	# def test15(self):
	# 	self.browser.find_element_by_link_text('Nonprofits').click()
	#
	# 	filter_button = self.browser.find_element_by_id("filter_bttn") # update word "filter" once implemented
	# 	filter_button.click()
	#
	# 	# might need a time/sleep here
	# 	selection = self.browser.find_element_by_id("selection") # update word "selection" once implemented
	# 	selection.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text('Nonprofit Name').click() # update word "specific_select" once implemented
	# 		self.assertEqual("http://npolink.me/nonprofit/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the sorting for the Nonprofits page
	# def test16(self):
	# 	self.browser.find_element_by_link_text('Nonprofits').click()
	#
	# 	sort_button = self.browser.find_element_by_id("sort_bttn") # update word "filter" once implemented
	# 	sort_button.click()
	#
	# 	# might need a time/sleep here
	# 	selection = self.browser.find_element_by_id("selection") # update word "selection" once implemented
	# 	selection.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text('Nonprofit Name').click() # update word "specific_select" once implemented
	# 		self.assertEqual("http://npolink.me/nonprofit/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the search for the Locations page
	# def test17(self):
	# 	self.browser.find_element_by_link_text('Locations').click()
	#
	# 	search_field = self.browser.find_element_by_id("search_bar") # update word "keywords" once implemented
	# 	search_field.click()
	# 	search_field.send_keys("") # send in some type of wording
	#
	# 	# might need a time/sleep here
	# 	search_button = self.browser.find_element_by_id("submit_button") # update word "keywords" once implemented
	# 	search_buttom.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text('Location Name').click() # update word "keywords" once implemented
	# 		self.assertEqual("http://npolink.me/location/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the filtering for the Locations page
	# def test18(self):
	# 	self.browser.find_element_by_link_text('Locations').click()
	#
	# 	filter_button = self.browser.find_element_by_id("filter_bttn") # update word "filter" once implemented
	# 	filter_button.click()
	#
	# 	# might need a time/sleep here
	# 	selection = self.browser.find_element_by_id("selection") # update word "selection" once implemented
	# 	selection.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text('Location Name').click() # update word "keywords" once implemented
	# 		self.assertEqual("http://npolink.me/location/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the sorting for the Locations page
	# def test19(self):
	# 	self.browser.find_element_by_link_text('Locations').click()
	#
	# 	sort_button = self.browser.find_element_by_id("sort_bttn") # update word "filter" once implemented
	# 	sort_button.click()
	#
	# 	# might need a time/sleep here
	# 	selection = self.browser.find_element_by_id("selection") # update word "selection" once implemented
	# 	selection.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text('Location Name').click() # update word "keywords" once implemented
	# 		self.assertEqual("http://npolink.me/location/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the search for the Categories page
	# def test20(self):
	# 	self.browser.find_element_by_link_text('Categories').click()
	#
	# 	search_field = self.browser.find_element_by_id("search_bar") # update word "keywords" once implemented
	# 	search_field.click()
	# 	search_field.send_keys("water")
	#
	# 	# might need a time/sleep here
	# 	search_button = self.browser.find_element_by_id("submit_button") # update word "keywords" once implemented
	# 	search_buttom.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text("Category Name").click() # update word "keywords" once implemented
	# 		self.assertEqual("http://npolink.me/category/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the filtering for the Categories page
	# def test21(self):
	# 	self.browser.find_element_by_link_text('Categories').click()
	#
	# 	filter_button = self.browser.find_element_by_id("filter_bttn") # update word "filter" once implemented
	# 	filter_button.click()
	#
	# 	# might need a time/sleep here
	# 	selection = self.browser.find_element_by_id("selection") # update word "selection" once implemented
	# 	selection.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text("Category Name").click() # update word "keywords" once implemented
	# 		self.assertEqual("http://npolink.me/category/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")
	#
	# # Tests the sorting for the Categories page
	# def test22(self):
	# 	self.browser.find_element_by_link_text('Categories').click()
	#
	# 	sort_button = self.browser.find_element_by_id("sort_bttn") # update word "filter" once implemented
	# 	sort_button.click()
	#
	# 	# might need a time/sleep here
	# 	selection = self.browser.find_element_by_id("selection") # update word "selection" once implemented
	# 	selection.click()
	#
	# 	# might need a time/sleep here
	# 	try:
	# 		self.browser.find_element_by_link_text("Category Name").click() # update word "keywords" once implemented
	# 		self.assertEqual("http://npolink.me/category/", self.browser.current_url) # update expected url once implemented
	# 	except NoSuchElementException:
	# 		self.fail("The element doesn't exist")

	def endBrowser(self):
		self.browser.quit()

if __name__ == "__main__":
	unittest.main()
