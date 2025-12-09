# Step-by-Step Setup Guide

Follow these steps to get your e-commerce website up and running:

## Prerequisites

Before starting, make sure you have:
- Python 3.8 or higher installed
- pip (Python package installer)

To check if Python is installed, open your terminal/command prompt and type:
```bash
python --version
```
or
```bash
python3 --version
```

## Step 1: Open Terminal/Command Prompt

- **Windows**: Press `Win + R`, type `cmd`, and press Enter
- **Mac/Linux**: Open Terminal application

Navigate to your project directory:
```bash
cd C:\Users\krish\OneDrive\Desktop\ecommerce
```

## Step 2: Create a Virtual Environment (Recommended)

This keeps your project dependencies separate from other projects.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command line, indicating the virtual environment is active.

## Step 3: Install Dependencies

Install all required Python packages:
```bash
pip install -r requirements.txt
```

This will install:
- Django 4.2.7
- Pillow 10.1.0 (for image handling)

Wait for the installation to complete.

## Step 4: Set Up the Database

Django needs to create the database tables. Run these commands:

```bash
python manage.py makemigrations
```

This creates migration files. Then run:

```bash
python manage.py migrate
```

This creates the actual database file (`db.sqlite3`) with all necessary tables.

## Step 5: Create a Superuser (Admin Account) - Optional but Recommended

This allows you to access the admin panel to add products:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- Username (e.g., `admin`)
- Email address (optional)
- Password (enter twice - it won't show as you type)

**Note**: Make sure your password is strong and remember it!

## Step 6: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**Keep this terminal window open** - the server is now running!

## Step 7: Access Your Website

Open your web browser and go to:

- **Main Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Step 8: Add Products (Using Admin Panel)

1. Go to http://127.0.0.1:8000/admin/
2. Log in with the superuser credentials you created in Step 5
3. Click on **"Categories"** under the "SHOP" section
4. Click **"Add Category"** and create categories like:
   - Name: `Citrus`, Slug: `citrus` (auto-generated)
   - Name: `Berries`, Slug: `berries`
   - Name: `Tropical`, Slug: `tropical`
   - Click **"Save"** for each

5. Click on **"Products"** under the "SHOP" section
6. Click **"Add Product"** and fill in:
   - **Name**: e.g., "Fresh Oranges"
   - **Slug**: Will auto-generate from name (or enter manually)
   - **Description**: e.g., "Sweet and juicy oranges, perfect for breakfast"
   - **Price**: e.g., `4.99`
   - **Category**: Select a category from dropdown
   - **Stock**: e.g., `50`
   - **Image**: Click "Choose File" to upload a fruit image (optional)
   - Click **"Save"**

7. Repeat step 6 to add more products

## Step 9: Test Your Website

1. Go back to http://127.0.0.1:8000/
2. You should see your products listed
3. Try:
   - Clicking on a product to see details
   - Adding items to cart
   - Viewing your cart
   - Going through checkout (use test data)

## Troubleshooting

### "python is not recognized"
- Try using `python3` instead of `python`
- Make sure Python is installed and added to PATH

### "No module named 'django'"
- Make sure you activated the virtual environment (see Step 2)
- Run `pip install -r requirements.txt` again

### "Port 8000 is already in use"
- Stop any other Django servers running
- Or use a different port: `python manage.py runserver 8001`

### Can't access the website
- Make sure the server is running (Step 6)
- Check that you're using the correct URL: http://127.0.0.1:8000/
- Try http://localhost:8000/ instead

### Database errors
- Delete `db.sqlite3` file (if it exists)
- Run `python manage.py migrate` again

## Stopping the Server

When you're done testing:
- Go back to the terminal where the server is running
- Press `Ctrl + C` (or `Ctrl + Break` on Windows) to stop the server

## Next Steps

- Add more products with images
- Customize the design in `static/css/style.css`
- Add more features as needed
- Read the `README.md` for more information

## Quick Reference Commands

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Happy coding! 🍎🍊🍌



