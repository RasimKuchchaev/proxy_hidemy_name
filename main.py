# import chromedriver_binary
from selenium.webdriver.remote.webdriver import By
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def get_proxy_list():
    driver = uc.Chrome()
    driver.get(
        "https://hidemy.name/ru/proxy-list/?country=AFALAOARAMAUATBDBEBZBJBOBABWBRBGKHCACLCNCOCICWCYCZDKDOECEGGQFIFRGED"
        "EGTHNHKHUINIDIRIQILITJPKZKRLBLYMGMYYTMXMDNLNGPSPYPEPHPLROSARSSGSKESCHTWTZTHTGTTTRAEGBUSUZVEVNVGZW&maxtime=21#list")
    delay = 10
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'table_block')))

    table = driver.find_element(By.CLASS_NAME, 'table_block')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    proxy_list = []
    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        ip = cells[0].text
        port = cells[1].text
        country_city = cells[2].text
        speed = cells[3].text
        type_protocol = cells[4].text
        anonim = cells[5].text
        end_update = cells[6].text
        proxy_list.append({'ip':ip, 'port':port, 'country_city':country_city, 'speed':speed,
                           'type_protocol':type_protocol, 'anonim':anonim, 'end_update':end_update})
        print(ip, port, country_city, speed, type_protocol, anonim, end_update)
    driver.quit()
    # print(proxy_list)

    with open('proxy_list.csv', 'w',encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=['ip','port','country_city','speed','type_protocol','anonim','end_update'])
        writer.writeheader()
        writer.writerows(proxy_list)


def open_proxy_list():
    with open('proxy_list.csv', 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['ip']}:{row['port']}")


if __name__ == '__main__':
    get_proxy_list()
    # open_proxy_list()

