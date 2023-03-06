import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
c = 0
driver = webdriver.Chrome(executable_path="E:\\chromedriver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://nutrineat.com/indian-food-calories")

table = driver.find_element(By.CLASS_NAME, "entry-content")

rows = table.find_elements(By.TAG_NAME, "tr")

with open('food.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")

        if len(cols) == 6:
            c += 1
            Food_List = cols[0].text.strip()
            Portion = cols[1].text.strip()
            Calories = cols[2].text.strip()
            Carbohydrates = cols[3].text.strip()
            Protein = cols[4].text.strip()
            Total_Fat = cols[5].text.strip()
            if c == 1:
                writer.writerow([Food_List, Portion, Calories, Carbohydrates, Protein, Total_Fat])
            else:
                if Portion.isnumeric():
                    writer.writerow([Food_List, Portion, Calories, Carbohydrates, Protein, Total_Fat])
        else:
            continue
driver.close()
print('Data has been scraped and saved to food.csv.')
