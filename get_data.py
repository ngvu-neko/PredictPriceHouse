from selenium import webdriver

chrome_diver_path = "...."
driver = webdriver.Chrome(executable_path= chrome_diver_path)
driver.get("webname")

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
