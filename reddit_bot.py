#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By  # Add this import
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time
#import pyperclip
#
#
## Set up Chrome options to exclude automation
#chrome_options = Options()
#chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#
## Launch the Chrome browser
#driver = webdriver.Chrome(options=chrome_options)
#
#
##get new temp mail id
#chrome_options = Options()
#chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#
#driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://temp-mail.org/en/")
#copy_email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tm-body']/div[1]/div/div/div[2]/div[1]/form/div[1]/div/button[2]")))
#copy_email.click()
#
#
#
##reddit create new account
#driver.execute_script("window.open('');")
#driver.switch_to.window(driver.window_handles[1])
#driver.get("https://www.reddit.com/register/")
#text_box = driver.find_element(By.XPATH, "//*[@id='regEmail']") 
#text_box.send_keys(pyperclip.paste())
#time.sleep(5)   
#enter_button = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[2]/button")
#time.sleep(5)   
#enter_button.click()
#time.sleep(5)   
#name_suggest = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/div[2]/div/div/a[1]")
#time.sleep(5)   
#name_suggest.click()   
#time.sleep(5)   
#password_field = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/div[1]/form/fieldset[2]/input[2]")
#time.sleep(5)   
#password_field.send_keys("143India<3")
#time.sleep(5);
#confirm_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[3]/button")
#time.sleep(5);
#confirm_button.click()
#
##reddit current user
#driver.execute_script("window.open('');")
#driver.switch_to.window(driver.window_handles[2])
#driver.get("https://www.reddit.com/r/aws/comments/1b3x41a/endless_security_checks/")
#time.sleep(5)
#hamburger_menu = driver.find_element(By.XPATH, "//*[@id='t3_1b3yqc1']/div[1]/span[2]/shreddit-async-loader[2]/shreddit-post-overflow-menu//div/faceplate-dropdown-menu/button")
#time.sleep(5)
#hamburger_menu.click()
#report_button = driver.find_element(By.XPATH, "//*[@id='t3_1b3x41a']/div[1]/span[2]/shreddit-async-loader[2]/shreddit-post-overflow-menu//div/faceplate-dropdown-menu/faceplate-menu/li[4]/div")
#report_button.click()
#time.sleep(5)
#content_button = driver.find_element(By.XPATH, "//*[@id='landingPage']/div[2]/div/button[3]")
#time.sleep(5)
#content_button.click()
#time.sleep(5)
#submit_button = driver.find_element(By.XPATH, "//*[@id='landingPage']/div[4]/div/report-action//button")
#time.sleep(5)
#submit_button.click()
#time.sleep(5)
#icon_button = driver.find_element(By.XPATH, "//*[@id='expand-user-drawer-button']")
#time.sleep(5)
#icon_button.click()
#time.sleep(5)
#logout_button = driver.find_element(By.XPATH,"//*[@id='logout-list-item']/div")
#time.sleep(5)
#
#
#
#
#
## Wait for a few seconds
#time.sleep(60)  # Adjust the time as needed
#
## Close the browser
#driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip


# Set up Chrome options to exclude automation
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Launch the Chrome browser
driver = webdriver.Chrome(options=chrome_options)

#get new temp mail id
driver.get("https://temp-mail.org/en/")
copy_email = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='click-to-copy']")))
copy_email.click()
temp_email = pyperclip.paste()

# Open a new tab for Reddit registration
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.reddit.com/register/")

# Register with the temporary email
text_box = driver.find_element(By.XPATH, "//*[@id='regEmail']") 
text_box.send_keys(temp_email)
time.sleep(7)   
enter_button = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[2]/button")
time.sleep(7)   
enter_button.click()
time.sleep(7)   
name_suggest = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/div[2]/div/div/a[1]")
time.sleep(7)   
name_suggest.click()   
time.sleep(7)   
password_field = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/div[1]/form/fieldset[2]/input[2]")
time.sleep(7)   
password_field.send_keys("143India<3")
time.sleep(7);
confirm_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[3]/button")
time.sleep(7);
confirm_button.click()

#Switch back to the main window

driver.switch_to.window(driver.window_handles[0])

# Open a new tab for Reddit current user interaction
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.reddit.com/r/aws/comments/1b3x41a/endless_security_checks/")
# button_element = driver.find_element_by_class_name("button-small")
time.sleep(13)
button_element=driver.find_element(By.XPATH, "//*[@id='t3_1b3x41a']/div[1]/span[2]/shreddit-async-loader[2]/shreddit-post-overflow-menu//div/faceplate-dropdown-menu/button")
button_element.click()
time.sleep(5)
hamburger_menu=driver.find_element(By.XPATH,"//*[@id='t3_1b3x41a']/div[1]/span[2]/shreddit-async-loader[2]/shreddit-post-overflow-menu//div/faceplate-dropdown-menu")
hamburger_menu.click()
print("menu clicked")
time.sleep(5)
report_button = driver.find_element(By.XPATH, "//*[@id=t3_1b43ca8'/div[1]/span[2]/shreddit-async-loader[2]/shreddit-post-overflow-menu//div/faceplate-dropdown-menu/faceplate-menu/li[4]/div")
report_button.click()
time.sleep(5)
content_button = driver.find_element(By.XPATH, "//*[@id='landingPage']/div[2]/div/button[3]")
time.sleep(5)
content_button.click()
time.sleep(5)
submit_button = driver.find_element(By.XPATH, "//*[@id='landingPage']/div[4]/div/report-action//button")
time.sleep(5)
submit_button.click()
time.sleep(5)
icon_button = driver.find_element(By.XPATH, "//*[@id='expand-user-drawer-button']")
time.sleep(5)
icon_button.click()
time.sleep(5)
logout_button = driver.find_element(By.XPATH,"//*[@id='logout-list-item']/div")
time.sleep(5)
# Wait for a few seconds
time.sleep(60)  # Adjust the time as needed

# Close the browser
driver.quit()
