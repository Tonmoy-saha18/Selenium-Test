from selenium import webdriver
from selenium.webdriver.firefox.service import Service as fireService
from webdriver_manager.firefox import GeckoDriverManager
browser = webdriver.Firefox(service=fireService(GeckoDriverManager().install()))
browser.get('http://www.facebook.com')