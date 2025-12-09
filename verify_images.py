"""
Quick script to verify all products have images
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitshop.settings')
django.setup()

from shop.models import Product

print("Checking product images...")
print("-" * 60)

products = Product.objects.all()

if not products.exists():
    print("No products found!")
else:
    for product in products:
        if product.image:
            print(f"✓ {product.name}: Has image")
            print(f"  URL: {product.image[:80]}...")
        else:
            print(f"✗ {product.name}: NO IMAGE")
        print()

print("-" * 60)
print(f"Total products: {products.count()}")
print(f"Products with images: {products.exclude(image='').exclude(image__isnull=True).count()}")



