import random
import time

from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By

def login(self):
    """Login to Path of Exil - POE"""
    try:
        self.browser.get("https://HIDDEN-URL.com/login?redirect_url=%2F")URL
        # HIDDEN-URL for security change it to your login domain
        time.sleep(random.uniform(5, 10))
        #self.browser.find_element_by_id("EmailInput_emailInput__4v_bn").send_keys(self.email)
        #self.browser.find_element_by_css_selector("Button_buttonBase__0QP_m Button_primary__pIDjn").click()
        #self.browser.find_element_by_id("VerificationCodeInput_verificationCodeInput__YD3KV").send_keys(self.password)
        #self.browser.find_element_by_css_selector("Button_buttonBase__0QP_m Button_primary__pIDjn").click()
        # due to I can't get active code via email then...we will login via Gmail.
        #login with GMAIL, remember comment 
        self.browser.find_element_by_css_selector("Button_buttonBase__0QP_m Button_tertiary__yq3dG ContinueWithGoogleButton_buttonContentWrapper__Mrp0W").click()
        #google auth page
        self.browser.find_element_by_css_selector("lCoei YZVTmd SmR8").click()
        time.sleep(random.uniform(5, 10))
    except TimeoutException:
        raise Exception("Could not login!")
