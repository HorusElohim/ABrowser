from pathlib import Path
import os

PKG = "ABrowser"

# Install folder
INSTALL_ROOT_PATH = Path().home() / PKG
# Ensure safe install location
os.makedirs(INSTALL_ROOT_PATH, exist_ok=True)

# Current pkg path
PKG_CWD_PATH = Path().cwd()


