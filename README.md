# New Store

- [BADGE HERE]
- [LICENSE]
- [CONTRIBUTION]

**New Store**: A personal project that simulates an appliance e-commerce platform. Developed using Django, PostgreSQL, and styled with Tailwind CSS for a modern and responsive user experience.

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
