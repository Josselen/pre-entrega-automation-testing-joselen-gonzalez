from selenium.webdriver.common.by import By

# Función auxiliar para realizar login en SauceDemo
def login(driver):
    #Ingresa el nombre de usuario y contraseña, luego hace click en el botón de login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()