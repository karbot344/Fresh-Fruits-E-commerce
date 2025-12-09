"""
Quick script to add sample categories and products to your database.
Run this after creating your superuser and running migrations.

Usage: python add_sample_data.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitshop.settings')
django.setup()

from shop.models import Category, Product

def add_sample_data():
    print("Adding sample categories and products...")
    print("-" * 50)
    
    # Create categories
    categories_data = [
        {'name': 'Citrus', 'slug': 'citrus'},
        {'name': 'Berries', 'slug': 'berries'},
        {'name': 'Tropical', 'slug': 'tropical'},
        {'name': 'Stone Fruits', 'slug': 'stone-fruits'},
        {'name': 'Apples & Pears', 'slug': 'apples-pears'},
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        categories[cat_data['slug']] = category
        if created:
            print(f"✓ Created category: {category.name}")
        else:
            print(f"→ Category already exists: {category.name}")
    
    print("-" * 50)
    
    # Create products
    products_data = [
        {
            'name': 'Fresh Oranges',
            'slug': 'fresh-oranges',
            'description': 'Sweet and juicy oranges, perfect for breakfast or snacks. Rich in vitamin C and naturally delicious.',
            'price': 424.15,  # $4.99 * 85
            'category': categories['citrus'],
            'stock': 50,
            'image': 'https://images.unsplash.com/photo-1619566636858-adf3ef46400b?w=500'
        },
        {
            'name': 'Strawberries',
            'slug': 'strawberries',
            'description': 'Plump, red strawberries picked at peak ripeness. Perfect for desserts or fresh eating.',
            'price': 509.15,  # $5.99 * 85
            'category': categories['berries'],
            'stock': 30,
            'image': 'https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=500'
        },
        {
            'name': 'Mangoes',
            'slug': 'mangoes',
            'description': 'Sweet and aromatic tropical mangoes. A perfect summer treat packed with flavor.',
            'price': 594.15,  # $6.99 * 85
            'category': categories['tropical'],
            'stock': 25,
            'image': 'https://images.unsplash.com/photo-1605027990121-1c0e0a0a5c5e?w=500'
        },
        {
            'name': 'Peaches',
            'slug': 'peaches',
            'description': 'Juicy and sweet peaches with a perfect balance of flavor. Great for snacking or baking.',
            'price': 466.65,  # $5.49 * 85
            'category': categories['stone-fruits'],
            'stock': 40,
            'image': 'https://images.unsplash.com/photo-1603279087175-0a3c8b0b5c5e?w=500'
        },
        {
            'name': 'Blueberries',
            'slug': 'blueberries',
            'description': 'Fresh blueberries packed with antioxidants. Great for smoothies or snacking.',
            'price': 679.15,  # $7.99 * 85
            'category': categories['berries'],
            'stock': 35,
            'image': 'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=500'
        },
        {
            'name': 'Lemons',
            'slug': 'lemons',
            'description': 'Fresh, tangy lemons perfect for cooking, baking, or making lemonade.',
            'price': 339.15,  # $3.99 * 85
            'category': categories['citrus'],
            'stock': 60,
            'image': 'https://images.unsplash.com/photo-1603279087175-0a3c8b0b5c5e?w=500'
        },
        {
            'name': 'Apples',
            'slug': 'apples',
            'description': 'Crisp and sweet apples, perfect for snacking. Available in various varieties.',
            'price': 381.65,  # $4.49 * 85
            'category': categories['apples-pears'],
            'stock': 45,
            'image': 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=500'
        },
        {
            'name': 'Grapes',
            'slug': 'grapes',
            'description': 'Sweet and juicy grapes, perfect for snacking or making wine.',
            'price': 551.65,  # $6.49 * 85
            'category': categories['berries'],
            'stock': 30,
            'image': 'https://images.unsplash.com/photo-1599599810769-bcde5a160d32?w=500'
        },
    ]
    
    for prod_data in products_data:
        product, created = Product.objects.get_or_create(
            slug=prod_data['slug'],
            defaults=prod_data
        )
        if created:
            print(f"✓ Created product: {product.name} - ₹{product.price}")
        else:
            print(f"→ Product already exists: {product.name}")
    
    print("-" * 50)
    print("\n✅ Sample data added successfully!")
    print(f"   Total Categories: {Category.objects.count()}")
    print(f"   Total Products: {Product.objects.count()}")
    print("\nVisit http://127.0.0.1:8000/ to see your products!")

if __name__ == '__main__':
    try:
        add_sample_data()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you've run migrations first:")
        print("  python manage.py migrate")

