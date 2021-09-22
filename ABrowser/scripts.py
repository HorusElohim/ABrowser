from ABrowser import BrowserFactory, DRIVER_PATH, PKG, OPTIONS_PATH
from IPython import embed
from pathlib import Path
import pkg_resources as pkg
import argparse
import yaml


def load_pkg_option_path(option):
    return pkg.resource_string(PKG, f'selen/options/{option}')


def write_text(path: Path, text):
    with open(path, 'wb') as fd:
        fd.write(text)


def install_options(option_file):
    write_text(OPTIONS_PATH / option_file, load_pkg_option_path(option_file))


def install_pkg_options():
    install_options('chrome_base.yml')


def list_file(path: Path, name=False):
    if name:
        return [x.name for x in path.iterdir() if x.is_file()]
    else:
        return [x for x in path.iterdir() if x.is_file()]


def installed_options(name=False):
    return list_file(OPTIONS_PATH, name)


def installed_drivers(name=False):
    return list_file(DRIVER_PATH, name)


def manage_option_arg(arg_option) -> dict:
    driver_option = dict()
    if arg_option:
        try:
            driver_option = yaml.load(pkg.resource_string(PKG, f'selen/options/{arg_option}'), Loader=yaml.SafeLoader)
        except Exception as e:
            print(f"Exception loading the options -> {e}")
    else:
        print("No options were provided. Use -opt <option_name>")
    return driver_option


def manage_browser_arg(arg_browser) -> Path:
    driver_path = None
    if len(installed_drivers()) == 0:
        print('No driver installed. Run: "ABrowser_drivers"')
    else:
        if arg_browser:
            driver_path = DRIVER_PATH / arg_browser
            if driver_path.exists():
                print("Driver selected correctly")
            else:
                print("The chosen driver is not installed.")
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
    PhantomJS : https://phantomjs.org/download.html
    """
    print(f'{driver_list}')
    print(f"The driver should be placed to this folder: {DRIVER_PATH}\n")
    print(f"Currently installed: {installed_drivers(name=True)}")


def ABrowser_options():
    print("ABrowser Options installation")
    print("All Chrome option available: https://peter.sh/experiments/chromium-command-line-switches/")
    print("Installing base options profile...")
    install_pkg_options()
    print(f"Store as yaml file the chosen one in the options folder: {OPTIONS_PATH}")
    print("Then pass the name of the json file with the -c option.")
    print(f"Currently installed: {installed_options(name=True)}")


def ABrowser_console():
    parser = argparse.ArgumentParser(prog="ABrowser", description='ABrowser python console')
    parser.add_argument("-d", "--driver", help=f"browser driver name. Stored in {DRIVER_PATH}", type=str)
    parser.add_argument("-o", "--options", help=f"options yaml name stored in {OPTIONS_PATH}", type=str)
    args = parser.parse_args()

    # Driver Options
    driver_option = manage_option_arg(args.options)
    # Driver path
    driver_path = manage_browser_arg(args.driver)

    if driver_path:
        ab = BrowserFactory.new(driver_path, driver_option)
        embed(colors="neutral")
        ab.close()
