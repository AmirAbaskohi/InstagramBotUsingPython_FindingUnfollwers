from selenium import webdriver
import time

class InstaBot:
	def __init__(self, username, password):
		self.driver = webdriver.Chrome("chromedriver.exe")
		self.driver.get("https://instagram.com")
		self.username = username
		self.password = password
		self.followings = []
		self.followers = []
		time.sleep(2)
		#self.driver.find_element_by_xpath("//span[contains(text(), 'Sign up')]").click()
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		time.sleep(10)
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		time.sleep(2)
	def getfollowings(self):
		self.driver.find_element_by_xpath("//a[contains(text(), '" + self.username + "')]").click()
		time.sleep(10)
		self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
		time.sleep(2)
		# sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
		# self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
		# time.sleep(5)
		scrollBox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
		lastHt,ht = 0,1
		while lastHt != ht:
			lastHt = ht
			time.sleep(5)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scrollBox)
		links = scrollBox.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']
		time.sleep(5)
		self.following = names
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
		time.sleep(5)

	def getfollowers(self):
		time.sleep(10)
		self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
		time.sleep(2)
		scrollBox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
		lastHt,ht = 0,1
		while lastHt != ht:
			lastHt = ht
			time.sleep(5)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scrollBox)
		links = scrollBox.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']
		self.followers = names
		print(self.followers)
		time.sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
		time.sleep(5)
	
	def getUnfollowers(self):
		for name in self.following:
			if name not in self.followers:
				print(name)

print("Welcome to my bot!It's made by MissMe")
username = input("Please Enter Your Username : ")
password = input("Please Enter Your Password : ")
myBot = InstaBot(username, password)
myBot.getfollowings()
myBot.getfollowers()
myBot.getUnfollowers()