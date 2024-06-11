import pytest 
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures('setup', 'tag_decoder')
class Test_EMV_Tag_Decoder():

    emv_tag_decoder_loc = (By.CSS_SELECTOR, "button[data-bs-target='#emv-tag-decoders-collapse']")
    div_emv_tag_loc = (By.XPATH, "//div[@class='pb-1 collapse show']/ul/li")
    input_tvr_loc = (By.XPATH, "//input[@id='input-tvr']")
    btn_tvr_loc = (By.CSS_SELECTOR, "#button-tvr-decode")
    div_tvr_decoded_loc = (By.CSS_SELECTOR, "#tvr-decoded")
    flat_tvr_loc = (By.ID, "input-tvr-flat")
    
    def test_expand_emv_tag_decoder(self):
        emv_tags = [ele.text for ele in self.driver.find_elements(*Test_EMV_Tag_Decoder.div_emv_tag_loc)]

        assert "TVR (Tag 95)" in emv_tags, "TVR (Tag 95) Decoder is listed"

    def test_tvr_clicked(self, tvr_decoder):
        assert self.driver.find_element(*Test_EMV_Tag_Decoder.input_tvr_loc), "TVR Decoder Clicked"

        
    def test_tvr_decoded(self, tvr_decoder):
        inp_tvr = self.driver.find_element(*Test_EMV_Tag_Decoder.input_tvr_loc)
        inp_tvr.send_keys("8000000000")
        tvr_decoded = self.driver.find_element(*Test_EMV_Tag_Decoder.div_tvr_decoded_loc)

        if not any(tvr_decoded.find_elements(By.CSS_SELECTOR, "*")):
            self.driver.find_element(*Test_EMV_Tag_Decoder.btn_tvr_loc).click()

        assert any(tvr_decoded.find_elements(By.CSS_SELECTOR, "*"))

        self.driver.find_element(*Test_EMV_Tag_Decoder.flat_tvr_loc).click()

        tvr_byte_1_bit_8 = tvr_decoded.find_element(By.XPATH, "//div/div[1]/table/tbody/tr[2]/td[1]/span").text

        assert tvr_byte_1_bit_8 == "2", "TVR Byte 1 Bit 8 is set to 1"

        tvr_byte_1_bit_8_highlighted = tvr_decoded.find_element(By.XPATH, "//div/div[1]/table/tbody/tr[2]/td[9]/span").get_attribute('class')

        assert tvr_byte_1_bit_8_highlighted == "bgset", "Offline data authentication was not performed"