from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

opt = webdriver.ChromeOptions()
preferences = {"directory_upgrade": True,
               "safebrowsing.enabled": True }
opt.add_experimental_option("prefs", preferences)
opt.add_extension('/mnt/c/Users/PATRICE LANSIAUX/AppData/Local/Google/Chrome/User Data/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.7.1_0.crx')
driver = webdriver.Chrome(chrome_options=opt,executable_path=r'/mnt/c/bin/chromedriver.exe')
EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

#hack 


# executor_url = driver.command_executor._url
# session_id = driver.session_id

def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver



#Interacting with metamask


#Interacting with the form
def fullfill():
  url = "https://vittominacori.github.io/bep20-generator/create-token/"
  driver.get(url)

  name = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[1]/div/div[2]/span[1]/div/div/input")
  name.send_keys("HVSE")

  symbol = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[1]/div/div[2]/span[2]/div/div/input")
  symbol.send_keys("HVSE")

  token = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div[1]/div[2]/div[1]/div/select")
  tokensub = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div[1]/div[2]/div[1]/div/select/option[1]")
  tokensub.click()

  network = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div[1]/div[2]/div[2]/div/select")
  NETWORK = "BSCT"
  if NETWORK == "BSCT":
    networksub = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div[1]/div[2]/div[2]/div/select/option[2]")
  if NETWORK == "BSC":
    networksub = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div[1]/div[2]/div[2]/div/select/option[1]")
  networksub.click()

  agree = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div[2]/div[2]/span/div/div/div")
  agree.click()

  submit = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/form/fieldset/div/div[3]/button")
  submit.click()

#
