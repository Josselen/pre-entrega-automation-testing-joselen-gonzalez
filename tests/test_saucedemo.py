from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login


def test_login_exitoso():
    # Inicializa navegador
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com")
    
    # Realiza login reutilizando helper
    login(driver)

    wait.until(EC.url_contains("inventory.html"))

    assert "inventory.html" in driver.current_url

    driver.quit()
    

def test_catalogo_productos():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com")

    login(driver)

    wait.until(EC.url_contains("inventory.html"))

    titulo = driver.find_element(By.CLASS_NAME, "title").text
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    nombre_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")


    assert menu.is_displayed()
    assert filtro.is_displayed()
    assert titulo == "Products"
    assert len(productos) > 0
    assert nombre_primer_producto != ""
    assert precio_primer_producto != ""

    driver.quit()


def test_agregar_producto_al_carrito():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com")

    login(driver)

    wait.until(EC.url_contains("inventory.html"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador_carrito == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.url_contains("cart.html"))

    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == "Sauce Labs Backpack"

    driver.quit()