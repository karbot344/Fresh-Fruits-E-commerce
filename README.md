# Fresh Fruits E-Commerce Website

A modern, responsive e-commerce website for selling fresh fruits built with Django, HTML, CSS, and JavaScript.

## Features

- **Product Catalog**: Browse fruits by category with search functionality
- **Product Details**: View detailed information about each fruit
- **Shopping Cart**: Add, update, and remove items from cart
- **Checkout Process**: Complete order placement with shipping information
- **Order Confirmation**: View order details after placement
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Beautiful and intuitive user interface

## Technologies Used

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default, can be changed)
- **Image Handling**: Pillow

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd ecommerce
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the website**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Setting Up Products

1. Log in to the admin panel at http://127.0.0.1:8000/admin/
2. Create categories (e.g., "Citrus", "Berries", "Tropical")
3. Add products with images, descriptions, prices, and stock quantities

## Project Structure

```
ecommerce/
├── fruitshop/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/               # Main app
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin configuration
│   └── templates/      # HTML templates
│       └── shop/
├── static/             # Static files
│   ├── css/
│   └── js/
├── media/              # User uploaded files (created automatically)
├── manage.py
└── requirements.txt
```

## Features in Detail

### Product Listing
- View all available fruits
- Filter by category
- Search by name or description
- Responsive grid layout

### Shopping Cart
- Add products to cart
- Update quantities
- Remove items
- View cart total
- Session-based cart (works without login)

### Checkout
- Enter shipping information
- Form validation
- Order placement
- Order confirmation page

## Customization

### Adding Products via Admin
1. Go to admin panel
2. Navigate to "Products"
3. Click "Add Product"
4. Fill in:
   - Name
   - Description
   - Price
   - Category
   - Stock quantity
   - Image (optional)

### Styling
- Main stylesheet: `static/css/style.css`
- CSS variables in `:root` for easy color customization

### JavaScript
- Main script: `static/js/main.js`
- Handles cart operations, notifications, and form validation

## Production Deployment

Before deploying to production:

1. **Update SECRET_KEY** in `fruitshop/settings.py`
2. **Set DEBUG = False** in `fruitshop/settings.py`
3. **Configure ALLOWED_HOSTS** in `fruitshop/settings.py`
4. **Set up a production database** (PostgreSQL recommended)
5. **Configure static files** for production
6. **Set up media file storage** (AWS S3, etc.)
7. **Use environment variables** for sensitive data

## License

This project is open source and available for personal and commercial use.

## Support

For issues or questions, please check the Django documentation or create an issue in the project repository.



