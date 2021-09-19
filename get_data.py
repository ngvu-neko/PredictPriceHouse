from selenium import webdriver

chrome_diver_path = "../chromedriver_win32/chromedriver"
driver = webdriver.Chrome(executable_path= chrome_diver_path)
driver.get("https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=020&ta=13&jspIdFlg=patternShikugun&sc=13103&sc=13109&sc=13111&kb=1&kt=9999999&km=1&tb=0&tt=9999999&hb=0&ht=9999999&ekTjCd=&ekTjNm=&tj=0&kw=1&srch_navi=1&pn=2")

#find price of house
price_list = driver.find_elements_by_class_name('dottable-value')
price_lists = [] 
for i in price_list:
	price_lists.append(i.text)
print(price_lists)


#find time to go to the station
distance   = driver.find_elements_by_css_selector('.dottable-line dl dd') 
list_distances = []
for i in distance:
	if "徒歩" in i.text:
		list_distances.append(i.text)

print(list_distances)

# find are of house 
area = driver.find_elements_by_css_selector('.dottable-fix dl dd')
list_area = []
for i in area:
	if 'm2' in i.text:
		list_area.append(i.text)
print(list_area)


driver.quit()