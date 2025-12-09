"""
Script to add image URLs to all products in the database.
Uses high-quality fruit images from Unsplash.

Usage: python add_product_images.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitshop.settings')
django.setup()

from shop.models import Product

def add_product_images():
    """
    Update all products with appropriate image URLs
    """
    print("Adding images to products...")
    print("-" * 60)
    
    # Image URLs mapping - high quality fruit images from Unsplash
    product_images = {
        'fresh-oranges': 'https://images.unsplash.com/photo-1619566636858-adf3ef46400b?w=800&q=80',
        'strawberries': 'https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=800&q=80',
        'mangoes': 'https://images.unsplash.com/photo-1605027990121-1c0e0a0a5c5e?w=800&q=80',
        'peaches': 'https://images.unsplash.com/photo-1603279087175-0a3c8b0b5c5e?w=800&q=80',
        'blueberries': 'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=800&q=80',
        'lemons': 'https://images.unsplash.com/photo-1580836779848-5a7b8c4e0c41?w=800&q=80',
        'apples': 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=800&q=80',
        'grapes': 'https://images.unsplash.com/photo-1599599810769-bcde5a160d32?w=800&q=80',
    }
    
    # Get all products
    products = Product.objects.all()
    
    if not products.exists():
        print("No products found in the database.")
        print("Run 'python add_sample_data.py' to add sample products first.")
        return
    
    updated_count = 0
    
    for product in products:
        # Check if product has a matching image URL
        if product.slug in product_images:
            old_image = product.image or "No image"
            product.image = product_images[product.slug]
            product.save()
            
            print(f"✓ Added image to {product.name}")
            print(f"  Image URL: {product.image}")
            updated_count += 1
        else:
            # Try to find a generic fruit image or use a placeholder
            if not product.image:
                # Use a generic fruit basket image as fallback
                product.image = 'https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=800&q=80'
                product.save()
                print(f"✓ Added generic image to {product.name}")
                updated_count += 1
            else:
                print(f"→ {product.name} already has an image")
    
    print("-" * 60)
    print(f"\n✅ Updated {updated_count} product(s) with images!")
    print("\nRefresh your browser to see the new product images!")

if __name__ == '__main__':
    try:
        add_product_images()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you've run migrations first:")
        print("  python manage.py migrate")



