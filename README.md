<p align="center">
  <a href="https://github.com/tyronejosee/project_new_store#gh-light-mode-only" target="_blank">
    <img src="./static/favicon/logo_light.svg" alt="logo-light" width="80">
  </a>
  <a href="https://github.com/tyronejosee/project_new_store#gh-dark-mode-only" target="_blank">
    <img src="./static/favicon/logo_dark.svg" alt="logo-dark" width="80">
  </a>
</p>
<p align="center">
  <strong>New Store</strong>
  <br>
  A personal project that simulates an appliance e-commerce platform. Developed using <b>Django</b>, <b>PostgreSQL</b>, and styled with <b>Tailwind CSS</b> for a modern and responsive user experience.
<p>
<p align="center">
  <a href="#"><strong>Website (Coming Soon)</strong></a>
</p>
<p align="center">
    <a href="#">
    <img src="https://img.shields.io/badge/python-3.11.3-blue" alt="python-version">
    </a>
    <a href="#">
    <img src="https://img.shields.io/badge/django-4.2.4-blue" alt="django-version">
    </a>
    <a href="#">
    <img src="https://img.shields.io/badge/tailwindcss-3.3.2-blue" alt="tailwind-version">
    </a>
</p>

## Features

Key features of New Store include:

- Smart Search.
- User Registration.
- Shopping Cart.
- PayPal Payment Gateway.
- Inventory Management.
- Offers and Promotions.
- Responsive Design.

## Screenshots

- ![pending](pending)
- ![pending](pending)
- ![pending](pending)

## Installation

**1. Clone the repository**:

```bash
git clone git@github.com:tyronejosee/project_new_store.git
```

**2. Navigate to the project directory**:

```bash
cd project_new_store
```

**3. Create a virtual environment**:

```bash
python -m venv venv
```

**4. Activate the virtual environment**:

```bash
# Windows
venv\Scripts\activate

# Unix/Linux
source venv/bin/activate  
```

**5. Install dependencies**:

```bash
pip install -r requirements.txt
```

**6. Perform database migrations**:

```bash
python manage.py migrate
```

**7. Start the development server**:

```bash
python manage.py runserver
```

## Configuration

Environment variables.

```bash
# Create an environment variable file .env
cp .env.example .env

# Open .env and configure environment variables such as database settings and secret keys
```

## Usage

Create a superuser to access the admin panel.

```bash
python manage.py createsuperuser
```

Start the development server and log in to `admin`.

```bash
python manage.py runserver
http://localhost:8000/admin/
```

## Contribution

## License
