from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#add incognito mode to options

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

#Internet explorer# browser = webdriver.ie(executable_path=C:\Users\mbrink\Desktop\IEDriverServer_Win32_3.9.0)
browser = webdriver.Chrome(executable_path='/Users/matt/github/chromedriver', options=option)



browser.get('https://finance.yahoo.com/quote/FB?p=FB')

timeout = 100

try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='Va(m) C($finDarkLink) Wow(bw) Us(n)']"))) #This is specific to the website. It's just an element on the page that he presumed would load last, so if it's loaded the rest of the page has probably loaded (not the most professional way of doing it)
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
#Get all the title for the financial values
titles_element = browser.find_elements_by_xpath("//td[@class='C(black)']") #This gets the "Titles" as a selenium element. Then the next line shows how to get the titles from the element.
titles = [x.text for x in titles_element]

# This is what the above would look like written as a normal FOR loop (the above is just cleaner):
#titles = []
#for x in titles_element:
#        titles.append(ax.text)

print('titles:')
print(titles)

#get all of the financial values themselves
values_element = browser.find_elements_by_xpath("//td[@class='Ta(end) Fw(b)']")
values = [x.text for x in values_element] # same concept as for-loop/list-comprehension above

print('values:')
print(values, '\n')

# pair each title with its corresponding value using zip function and print each pair.
for title, value in zip(titles, values):
    print(title + ': ' + value)
