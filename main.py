import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from validate_email import validate_email
from botass import HuyRemy 


def init_browser():
    browser_options = Options()
    options = ['--disable-blink-features', '--no-sandbox', '--disable-extensions',
               '--ignore-certificate-errors', '--disable-blink-features=AutomationControlled']
    for option in options:
        #browser_options.add_argument(option)
        #options = selenium.webdriver.ChromeOptions()
        #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        #driver.set_window_position(0, 0)
        #driver.maximize_window()
        options = Options()
        driver  = webdriver.Firefox()
    return driver
def get_configuration():
    """
    Get input from configuration file and validate values.
    Return valid configuration or raise exception.
    """
    with open("config.yaml", 'r') as stream:
        try:
            parameters = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc
    login_params = ['EmailInput_emailInput__4v_bn', 'username', 'password']
  #Due to SMTP Server Poe.com get error, have no email send to me. Then i can't get param config
    for login_param in login_params:
        if login_param not in parameters:
            raise Exception(login_param + ' is not inside the yml file!')
    assert validate_email(parameters['EmailInput_emailInput__4v_bn'])
    assert len(str(parameters['username'])) > 0
    assert len(str(parameters['password'])) > 0
    return parameters
 
if __name__ == '__main__':
    parameters = get_configuration()
    browser = init_browser()
    bot = HuyRemy(parameters, browser)
    bot.login()
    #bot.continuous()
