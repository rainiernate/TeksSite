# TEKS Services Website

A custom Django website for TEKS Services print shop, offering printing, mailing, and marketing services.

## Features

- Responsive design using Bootstrap 5
- Content management system for services, testimonials, and blog posts
- Contact form for customer inquiries
- Portfolio showcase
- Blog with pagination

## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 5.2+
- Pillow (for image processing)

### Installation

1. Clone the repository:
```
git clone <repository-url>
cd TeksSite
```

2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```
pip install django pillow
```

4. Apply migrations:
```
cd teks_project
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser to access the admin panel:
```
python manage.py createsuperuser
```

6. Run the development server:
```
python manage.py runserver
```

7. Access the website at http://localhost:8000 and the admin panel at http://localhost:8000/admin

### Adding Content

After logging into the admin panel, you can add:

1. **Services**: Add printing, mailing, and marketing services
2. **Testimonials**: Add customer testimonials
3. **Blog Posts**: Create and publish blog articles
4. **Contact Requests**: View and manage customer inquiries

## Project Structure

- `print_shop/` - Main Django app
  - `models.py` - Database models
  - `views.py` - View functions and classes
  - `urls.py` - URL routing
  - `admin.py` - Admin interface configuration
  - `forms.py` - Form definitions
  - `templates/` - HTML templates
  - `static/` - CSS, JavaScript, and images

## Customization

- Edit templates in `print_shop/templates/print_shop/`
- Modify styles in `print_shop/static/print_shop/css/style.css`
- Update JavaScript in `print_shop/static/print_shop/js/main.js`

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure a proper database (PostgreSQL recommended)
3. Set up static files serving
4. Use a production web server like Nginx with Gunicorn

## License

This project is licensed under the MIT License - see the LICENSE file for details.
