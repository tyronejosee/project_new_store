# New Store

[BADGE HERE]
LICENCIAS
CONTRIBUCION

New Stores es una plataforma de comercio electrónico especializada en la venta de una amplia gama de electrodomésticos de alta calidad. Desarrollada en Python con el marco de trabajo Django, nuestra aplicación web ofrece a los usuarios una experiencia de compra intuitiva y segura. Una robusta base de datos PostgreSQL, inventario y pedidos, asegurando un flujo eficiente de datos. El diseño de la interfaz, implementado con Tailwind, proporciona una apariencia moderna y receptiva, mejorando la usabilidad y la experiencia del usuario en todas las pantallas y dispositivos.

[CAPTURAS]

## Características

- Búsqueda Inteligente: Nuestra función de búsqueda avanzada utiliza algoritmos de coincidencia para ayudar a los usuarios a encontrar rápidamente los productos que desean, incluso si cometen errores ortográficos.
- Gestión de Cuenta de Usuario: Los clientes pueden crear y administrar fácilmente sus cuentas de usuario, guardar información de envío y ver su historial de pedidos para una experiencia de compra personalizada.
- Carrito de Compras: Los usuarios pueden agregar y eliminar productos de su carrito de compras de manera sencilla, y ver un resumen de los productos seleccionados antes de la compra.
- Pasarela de pago con PayPal: Los usuarios pueden usar paypal como método de pago al momento de tener listo su carrito de compras.
- Gestión de Inventarios: Mantenemos un seguimiento en tiempo real del inventario de productos, lo que garantiza que los clientes puedan comprar productos disponibles y evita problemas de agotamiento de stock.
- Ofertas y Promociones: Publicamos ofertas y promociones especiales periódicamente, lo que permite a los clientes obtener descuentos y ahorrar en sus compras.
- Diseño Responsivo: Nuestra interfaz está diseñada con Django-Tailwind para ser completamente receptiva, lo que significa que los usuarios pueden comprar desde dispositivos móviles, tabletas o computadoras de escritorio sin problemas.

## Requisitos Previos

- Python 3.x
- Django 3.x
- PostgreSQL

## Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/tuproyecto.git
```

### 2. Entra al directorio del proyecto

```bash
cd tuproyecto
```

### 3. Crea un entorno virtual

```bash
python -m venv venv
```

### 4. Activa el entorno virtual

```bash
source venv/bin/activate  # En sistemas Unix/Linux
venv\Scripts\activate     # En Windows
```

### 5. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 6. Realiza las migraciones de la base de datos

```bash
python manage.py migrate
```

### 7. Inicia el servidor de desarrollo

```bash
python manage.py runserver
```

## Configuración

```bash
# Crea un archivo de variables de entorno .env
cp .env.example .env

# Abre .env y configura las variables de entorno, como la configuración de la base de datos y las claves secretas
```

## Uso

Detalla cómo utilizar y ejecutar el proyecto. Proporciona ejemplos de comandos o código para ejecutar las tareas comunes. Por ejemplo:

```bash
# Crea un superusuario para acceder al panel de administración
python manage.py createsuperuser

# Inicia el servidor de desarrollo
python manage.py runserver

# Accede al panel de administración en http://localhost:8000/admin/
```

## Contribución

## Licencia
