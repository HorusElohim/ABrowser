from pathlib import Path
from . import Chrome, Phantom


class BrowserFactory:
    @staticmethod
    def new(driver_path: Path, driver_option: dict):
        if 'chrome' in driver_path.name:
            return Chrome(driver_path, driver_option)
        elif 'phantom' in driver_path.name:
            return Phantom(driver_path, driver_option)
