@echo off
echo Installing dependencies for Windows...
echo.

echo Step 1: Upgrading pip...
python -m pip install --upgrade pip
echo.

echo Step 2: Installing setuptools and wheel...
python -m pip install --upgrade setuptools wheel
echo.

echo Step 3: Attempting to install Pillow...
python -m pip install Pillow
echo.

if %ERRORLEVEL% EQU 0 (
    echo Pillow installed successfully!
    echo.
    echo Step 4: Installing Django...
    python -m pip install Django==4.2.7
    echo.
    echo All dependencies installed successfully!
) else (
    echo.
    echo Pillow installation failed. Trying alternative method...
    echo.
    echo Attempting to install Pillow 9.5.0 (older version with better Windows support)...
    python -m pip install Pillow==9.5.0
    echo.
    if %ERRORLEVEL% EQU 0 (
        echo Pillow 9.5.0 installed successfully!
        echo Installing Django...
        python -m pip install Django==4.2.7
        echo.
        echo All dependencies installed successfully!
    ) else (
        echo.
        echo ========================================
        echo INSTALLATION FAILED
        echo ========================================
        echo.
        echo Please try one of these solutions:
        echo.
        echo Option 1: Install without Pillow (images won't work)
        echo   python -m pip install Django==4.2.7
        echo.
        echo Option 2: Install Microsoft C++ Build Tools
        echo   Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
        echo   Then run this script again
        echo.
        echo Option 3: Use Conda instead of pip
        echo   conda install pillow
        echo   pip install Django==4.2.7
        echo.
        echo See TROUBLESHOOTING.md for more details
        echo.
    )
)

pause



