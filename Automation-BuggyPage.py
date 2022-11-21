import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('https://buggy.justtestit.org/')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/my-app/div/main/my-home/div')))

# Logueo en la página (el usuario se creó con propósitos de testing)
btn_login = '/html/body/my-app/header/nav/div/my-login/div/form/button'
path_user = '/html/body/my-app/header/nav/div/my-login/div/form/div/input[1]'
path_pw = '/html/body/my-app/header/nav/div/my-login/div/form/div/input[2]'
user = 'jhon_testing'
pw = 'Aa.123456'
driver.find_element('xpath',path_user).send_keys(user)
driver.find_element('xpath',path_pw).send_keys(pw)
driver.find_element('xpath',btn_login).click()
wait.until(ec.visibility_of_element_located((By.XPATH,"/html/body/my-app/header/nav/div/my-login/div/ul/li[1]/span")))
print("Inicio de sensión exitoso")
time.sleep(1)

# Sección de Perfil
btn_profile = '/html/body/my-app/header/nav/div/my-login/div/ul/li[2]/a'
add_info = '/html/body/my-app/div/main/my-profile/div/form/div[1]/div[2]'
path_address = '//*[@id="address"]'
btn_cancel = '/html/body/my-app/div/main/my-profile/div/form/div[2]/div/a'

driver.find_element('xpath',btn_profile).click()
wait.until(ec.visibility_of_element_located((By.XPATH,add_info)))

add_info_view = driver.find_element('xpath',add_info)
add_info_view.location_once_scrolled_into_view
time.sleep(1)
driver.find_element('xpath',path_address).send_keys("Esto es solo para prueba, así que no modificaré nada y oprimiré cancelar. Los saluda Jhon Tafur")
time.sleep(3)

btn_cancel_view = driver.find_element('xpath',btn_cancel)
btn_cancel_view.location_once_scrolled_into_view
time.sleep(1)
driver.find_element('xpath',btn_cancel).click()
print("Revision de perfil exitosa")
makes_list = '/html/body/my-app/div/main/my-home/div'
wait.until(ec.visibility_of_element_located((By.XPATH, makes_list)))
time.sleep(1)
makes_list_view = driver.find_element('xpath',makes_list)
makes_list_view.location_once_scrolled_into_view
time.sleep(1)

# Inspección de sección Alfa Romeo
slc_alfarm = '/html/body/my-app/div/main/my-home/div/div[1]/div/a/img'
alfarm_cont = '/html/body/my-app/div/main/my-make/div'
car_guilia = '/html/body/my-app/div/main/my-make/div/div[2]/div/div/table/tbody/tr[1]/td[2]/a'
cars_list= '/html/body/my-app/div/main/my-make/div/div[2]/div/div'
car_guilia_img = '/html/body/my-app/div/main/my-model/div/div[1]/div[2]/div/a/img'
comments = '//*[@id="comment"]'
btn_home = '/html/body/my-app/header/nav/div/a'

driver.find_element('xpath',slc_alfarm).click()
wait.until(ec.visibility_of_element_located((By.XPATH,alfarm_cont)))
cars_list_view = driver.find_element('xpath',cars_list)
cars_list_view.location_once_scrolled_into_view
time.sleep(2)
driver.find_element('xpath',car_guilia).click()
wait.until(ec.visibility_of_element_located((By.XPATH,car_guilia_img)))
driver.find_element('xpath',comments).send_keys("Bonito pero no hay dinero :c volvamos a la página principal")
time.sleep(3)
driver.find_element('xpath',btn_home).click()
print("Inspección de Alfa Romeo exitosa")
wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/my-app/div/main/my-home/div')))
time.sleep(1)

btn_logout = '/html/body/my-app/header/nav/div/my-login/div/ul/li[3]/a'
driver.find_element('xpath',btn_logout).click()
time.sleep(2)
driver.find_element('xpath',path_user).send_keys("Hasta la próxima")
time.sleep(3)
driver.quit()