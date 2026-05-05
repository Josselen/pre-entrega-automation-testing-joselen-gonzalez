# Pre Entrega Automation Testing - SauceDemo

## 📌 Propósito del proyecto

Este proyecto corresponde a una pre-entrega de Automation Testing.  
El objetivo es automatizar casos de prueba sobre el sitio [SauceDemo](https://www.saucedemo.com/) utilizando Selenium WebDriver y Pytest.

Se automatizan los siguientes flujos:

- Login exitoso con credenciales válidas
- Validación del catálogo de productos
- Agregado de producto al carrito
- Verificación del producto dentro del carrito

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Selenium
- Pytest
- Pytest HTML
- Google Chrome

---

## 📁 Estructura del proyecto

```bash
pre-entrega-automation-testing-joselen-gonzalez/
├── tests/
│   └── test_saucedemo.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── reports/
│   └── reporte.html
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore 
```

⚙️ Instalación
Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate
Instalar dependencias
python3 -m pip install -r requirements.txt

▶️ Ejecución de pruebas
Ejecutar todas las pruebas
python3 -m pytest -v
Ejecutar pruebas y generar reporte HTML
python3 -m pytest -v --html=reports/reporte.html

🧪 Casos de prueba automatizados

🔐 Login exitoso
Navega a https://www.saucedemo.com/
Ingresa usuario válido: standard_user
Ingresa contraseña válida: secret_sauce
Valida redirección a inventario

🛒 Catálogo de productos
Valida título Products
Verifica productos visibles
Obtiene nombre y precio del primer producto
Valida menú y filtro

🧾 Carrito de compras
Agrega producto al carrito
Verifica contador = 1
Ingresa al carrito
Valida producto agregado

📊 Reporte

El reporte HTML de ejecución se genera en:

reports/reporte.html

👩‍💻 Autor
Joselen Gonzalez
