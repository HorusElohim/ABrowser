from ABrowser import Chrome, DRIVER_PATH, PKG
from IPython import embed
from pathlib import Path
import pkg_resources as pkg
import argparse
import yaml


def installed_drivers():
    return [x for x in DRIVER_PATH.iterdir() if x.is_file()]


def manage_option_arg(arg_option):
    driver_option = dict()
    if arg_option:
        try:
            driver_option = yaml.load(pkg.resource_string(PKG, f'selen/options/{arg_option}'), Loader=yaml.SafeLoader)
        except Exception as e:
            print(f"Exception loading the options -> {e}")
    else:
        print("No options were provided. Use -opt <option_name>")
    return driver_option


def manage_browser_arg(arg_browser):
    driver_path = None
    if len(installed_drivers()) == 0:
        print('No driver installed. Run: "ABrowser_drivers"')
    else:
        if arg_browser:
            if arg_browser == 'chrome':
                driver_path = DRIVER_PATH / 'chromedriver'
        else:
            print("No browser were provided. Use -b <browser_name>")
            driver_path = installed_drivers()[0]
            print(f"Default browser selected: {driver_path.name}")
    return driver_path


def ABrowser_drivers():
    print("ABrowser Driver installation")
    print(f"Download the suitable driver for your browser version:")
    driver_list = """
    Chrome : https://chromedriver.chromium.org/downloads
    FireFox : https://github.com/mozilla/geckodriver/releases
    """
    print(f'{driver_list}')
    print(f"The driver should be placed to this folder: {DRIVER_PATH}\n")
    print(f"Currently installed: {installed_drivers()}")


def ABrowser_console():
    parser = argparse.ArgumentParser(prog="ABrowser", description='ABrowser python console')
    parser.add_argument("-b", "--browser", help="type of browser", type=str)
    parser.add_argument("-opt", "--options", help="type of option", type=str)
    args = parser.parse_args()

    # Driver Options
    driver_option = manage_option_arg(args.options)
    # Driver path
    driver_path = manage_browser_arg(args.browser)

    if driver_path:
        ab = Chrome(driver_path, driver_option)
        embed(colors="neutral")
        ab.close()
