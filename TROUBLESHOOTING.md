# Troubleshooting Guide

## Pillow Installation Error on Windows

If you get an error like "ERROR: Failed to build 'Pillow'", try these solutions in order:

### Solution 1: Install Pre-built Wheel (Easiest)

Try installing Pillow separately with a pre-built wheel:

```bash
pip install --upgrade pip
pip install Pillow
```

If that doesn't work, try:

```bash
pip install --upgrade pip setuptools wheel
pip install Pillow
```

### Solution 2: Use a Different Pillow Version

Try installing a slightly older version that has better Windows support:

```bash
pip install Pillow==9.5.0
```

Then install the rest:

```bash
pip install -r requirements.txt --no-deps
pip install Django==4.2.7
```

### Solution 3: Install Build Tools (For Advanced Users)

If you have Visual Studio installed or want to install build tools:

1. Download and install **Microsoft C++ Build Tools** from:
   https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. During installation, select "C++ build tools" workload

3. Restart your terminal and try again:
   ```bash
   pip install -r requirements.txt
   ```

### Solution 4: Use Conda (Alternative)

If you have Anaconda or Miniconda installed:

```bash
conda install pillow
pip install Django==4.2.7
```

### Solution 5: Skip Pillow Temporarily (Quick Fix)

If you just want to get started quickly and don't need image uploads right away:

1. Edit `requirements.txt` and remove or comment out the Pillow line:
   ```
   Django==4.2.7
   # Pillow>=10.0.0
   ```

2. Install Django only:
   ```bash
   pip install Django==4.2.7
   ```

3. The website will work, but product images won't be uploadable through admin until Pillow is installed.

4. You can still add products without images, or add image URLs manually later.

### Solution 6: Use Python 3.11 or Lower

Sometimes newer Python versions have compatibility issues. If you're using Python 3.12+, try:

1. Create a new virtual environment with Python 3.11:
   ```bash
   python3.11 -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Other Common Issues

### "python is not recognized"
- Make sure Python is installed
- Try `python3` instead of `python`
- Add Python to your system PATH

### "pip is not recognized"
- Try `python -m pip` instead of just `pip`
- Or: `python3 -m pip install -r requirements.txt`

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Locked Error
- Close any other programs accessing the database
- Delete `db.sqlite3` and run migrations again

## Still Having Issues?

1. Make sure you're in the virtual environment (you should see `(venv)` in your prompt)
2. Update pip first: `python -m pip install --upgrade pip`
3. Try installing packages one by one to identify the problem



