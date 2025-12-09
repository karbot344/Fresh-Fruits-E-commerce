"""
Script to update existing product prices in the database to INR
using the exchange rate: 1 USD = ₹85

This script will:
1. Find all products that have prices that look like USD prices (under 100)
2. Convert them to INR by multiplying by 85
3. Update the database

Usage: python update_prices_to_inr.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitshop.settings')
django.setup()

from shop.models import Product

def update_prices_to_inr():
    """
    Update product prices from USD to INR using 1 USD = ₹85
    Assumes products with prices < 100 are in USD
    """
    exchange_rate = 85  # 1 USD = 85 INR
    
    print("Updating product prices to INR (1 USD = ₹85)...")
    print("-" * 60)
    
    # Get all products
    products = Product.objects.all()
    
    if not products.exists():
        print("No products found in the database.")
        print("Run 'python add_sample_data.py' to add sample products first.")
        return
    
    updated_count = 0
    
    for product in products:
        # Check if price looks like USD (less than 100, typically 3-10 range)
        if product.price < 100:
            old_price = product.price
            new_price = float(product.price) * exchange_rate
            product.price = round(new_price, 2)
            product.save()
            
            print(f"✓ Updated {product.name}:")
            print(f"  ${old_price:.2f} → ₹{product.price:.2f}")
            updated_count += 1
        else:
            print(f"→ Skipped {product.name}: ₹{product.price:.2f} (already in INR range)")
    
    print("-" * 60)
    print(f"\n✅ Updated {updated_count} product(s) to INR prices!")
    print(f"   Exchange rate used: 1 USD = ₹{exchange_rate}")
    print("\nAll prices are now in Indian Rupees (INR)")

if __name__ == '__main__':
    try:
        # Ask for confirmation
        print("\nThis will update all product prices in your database.")
        print("Products with prices < ₹100 will be multiplied by 85 (USD to INR conversion)")
        print("\nDo you want to continue? (yes/no): ", end='')
        
        response = input().strip().lower()
        
        if response in ['yes', 'y']:
            update_prices_to_inr()
        else:
            print("\nUpdate cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you've run migrations first:")
        print("  python manage.py migrate")



