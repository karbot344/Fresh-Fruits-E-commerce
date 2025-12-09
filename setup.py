"""
Quick setup script to initialize the Django project.
Run this after installing dependencies to set up the database.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitshop.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Category, Product

def create_sample_data():
    """Create sample categories and products for testing"""
    print("Creating sample data...")
    
    # Create categories
    categories_data = [
        {'name': 'Citrus', 'slug': 'citrus'},
        {'name': 'Berries', 'slug': 'berries'},
        {'name': 'Tropical', 'slug': 'tropical'},
        {'name': 'Stone Fruits', 'slug': 'stone-fruits'},
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        categories[cat_data['slug']] = category
        if created:
            print(f"Created category: {category.name}")
    
    # Create sample products
    products_data = [
        {
            'name': 'Fresh Oranges',
            'slug': 'fresh-oranges',
            'description': 'Sweet and juicy oranges, perfect for breakfast or snacks. Rich in vitamin C.',
            'price': 4.99,
            'category': categories['citrus'],
            'stock': 50
        },
        {
            'name': 'Strawberries',
            'slug': 'strawberries',
            'description': 'Plump, red strawberries picked at peak ripeness. Perfect for desserts or fresh eating.',
            'price': 5.99,
            'category': categories['berries'],
            'stock': 30
        },
        {
            'name': 'Mangoes',
            'slug': 'mangoes',
            'description': 'Sweet and aromatic tropical mangoes. A perfect summer treat.',
            'price': 6.99,
            'category': categories['tropical'],
            'stock': 25
        },
        {
            'name': 'Peaches',
            'slug': 'peaches',
            'description': 'Juicy and sweet peaches with a perfect balance of flavor.',
            'price': 5.49,
            'category': categories['stone-fruits'],
            'stock': 40
        },
        {
            'name': 'Blueberries',
            'slug': 'blueberries',
            'description': 'Fresh blueberries packed with antioxidants. Great for smoothies or snacking.',
            'price': 7.99,
            'category': categories['berries'],
            'stock': 35
        },
        {
            'name': 'Lemons',
            'slug': 'lemons',
            'description': 'Fresh, tangy lemons perfect for cooking, baking, or making lemonade.',
            'price': 3.99,
            'category': categories['citrus'],
            'stock': 60
        },
    ]
    
    for prod_data in products_data:
        product, created = Product.objects.get_or_create(
            slug=prod_data['slug'],
            defaults=prod_data
        )
        if created:
            print(f"Created product: {product.name}")
    
    print("\nSample data created successfully!")
    print("You can now run 'python manage.py runserver' to start the development server.")

if __name__ == '__main__':
    print("Setting up database...")
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')
    
    print("\nWould you like to create sample data? (y/n): ", end='')
    response = input().strip().lower()
    
    if response == 'y':
        create_sample_data()
    else:
        print("\nSetup complete! You can add products via the admin panel.")
        print("Create a superuser with: python manage.py createsuperuser")



