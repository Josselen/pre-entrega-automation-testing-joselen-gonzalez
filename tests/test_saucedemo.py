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

    # Espera redirección a inventario
    wait.until(EC.url_contains("inventory.html"))
    # Validación de login exitoso
    assert "inventory.html" in driver.current_url

    driver.quit()
    
# Test de validación del catálogo de productos
def test_catalogo_productos():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    # Abre la página de SauceDemo
    driver.get("https://www.saucedemo.com")
    # Realiza login 
    login(driver)
    # Espera redirección al inventario
    wait.until(EC.url_contains("inventory.html"))
    # Obtiene el título de la página 
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    # Obtiene todos los productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    # Obtiene nombre del primer producto y su precio
    nombre_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    # Valida presencia del menú lateral y del filtro de ordenamiento
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Verifica que el menu y el filtro estén visibles, el titulo sea correcto, que haya productos listados y que el primer producto tenga nombre y precio no vacíos
    assert menu.is_displayed()
    assert filtro.is_displayed()
    assert titulo == "Products"
    assert len(productos) > 0
    assert nombre_primer_producto != ""
    assert precio_primer_producto != ""
    # Cierra navegador
    driver.quit()

# Test de agregado de producto al carrito
def test_agregar_producto_al_carrito():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com")

    login(driver)

    wait.until(EC.url_contains("inventory.html"))
    # Agrega el producto Sauce Labs Backpack al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # Obtiene el contador del carrito
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    # Verifica que el contador sea 1
    assert contador_carrito == "1"
    # Ingresa al carrito de compras
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # Espera carga de la página del carrito
    wait.until(EC.url_contains("cart.html"))
    # Obtiene nombre del producto agregado al carrito
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == "Sauce Labs Backpack"

    driver.quit()