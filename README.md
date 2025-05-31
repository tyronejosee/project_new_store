<p align="center">
  <a href="https://github.com/tyronejosee/project_new_store#gh-light-mode-only" target="_blank">
    <img src="./static/img/logo_light.svg" alt="logo-light" width="80">
  </a>
  <a href="https://github.com/tyronejosee/project_new_store#gh-dark-mode-only" target="_blank">
    <img src="./static/img/logo_dark.svg" alt="logo-dark" width="80">
  </a>
</p>
<p align="center">
  <strong>New Store</strong>
  <br>
  A personal project that simulates an appliance e-commerce platform. Developed using <b>Django</b>, <b>PostgreSQL</b>, and styled with <b>Tailwind CSS</b> for a modern and responsive user experience.
<p>
<p align="center">
  <a href="https://new-store-8vlz.onrender.com/"><strong>Website (Render)</strong></a>
</p>
<p align="center">
  <a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/python-3.11.3-blue" alt="python-version">
  </a>
  <a href="https://www.djangoproject.com/">
  <img src="https://img.shields.io/badge/django-4.2.4-blue" alt="django-version">
  </a>
  <a href="https://tailwindcss.com/">
  <img src="https://img.shields.io/badge/tailwindcss-3.3.2-blue" alt="tailwind-version">
  </a>
  <a href="https://nodejs.org/en">
  <img src="https://img.shields.io/badge/node-18.17.1-blue" alt="tailwind-version">
  </a>
</p>

<a href="https://youtu.be/Lbd__Meplyg">
  <img src="http://i3.ytimg.com/vi/Lbd__Meplyg/maxresdefault.jpg">
</a>

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

![Main_Light](/static/img/main_light.webp)
![Main_Dark](/static/img/main_dark.webp)

[See more screenshots...](screenshots.md)

## Installation

### Project

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
python -m venv env
```

**4. Activate the virtual environment**:

```bash
# Windows
env\Scripts\activate

# Unix/Linux
source env/bin/activate
```

**5. Install dependencies**:

```bash
pip install -r requirements.txt
```

**6. Perform database migrations**:

Create the environment variables first, then run

```bash
python manage.py migrate
```

**7. Start the development server**:

```bash
python manage.py runserver
```

### Tailwind CSS

**1. Install Tailwind using npm ([Node.js](https://nodejs.org/en)** Required):

```bash
npm install -D tailwindcss
```

**2. Compile Tailwind CSS styles**:

```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

Remember not to run `npx tailwindcss init` because there are already predefined styles for this project, and this command will overwrite the `tailwind.config.js` file.

Use two terminals for a better workflow, one for compiling Tailwind and another for running the Django development server.

## Configuration

Create the environment variables.

```bash
# .env
SECRET_KEY=''
PYTHON_VERSION='3.11.7'
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
CLOUDINARY_CLOUD_NAME=''
CLOUDINARY_API_KEY=''
CLOUDINARY_API_SECRET=''
```

## Usage

Create a superuser to access the entire site without restrictions.

```bash
python manage.py createsuperuser
```

Start the development server and log in to `admin`.

```bash
python manage.py runserver
http://localhost:8000/admin/
```

## Tests

Run tests globally.

```bash
python manage.py test
```

Or run individual tests per app.

```bash
python manage.py test users
```

## License

This project is under the [Apache-2.0 license](https://github.com/tyronejosee/project_new_store/blob/main/LICENSE).
