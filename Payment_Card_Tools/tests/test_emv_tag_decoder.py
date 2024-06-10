import pytest 
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures('setup')
class Test_EMV_Tag_Decoder():

    emv_tag_decoder = (By.XPATH, "//button[normalize-space()='EMV Tag Decoders']")
    
    def test_expand_emv_tag_decoder(self):
        self.driver.find_element(*Test_EMV_Tag_Decoder.emv_tag_decoder).click()
        time.sleep(5)