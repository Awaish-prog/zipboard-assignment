import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DocumentPage:

    def __init__(self):
        self.annotate = (By.XPATH, '//button[@data-element="toolbarGroup-Annotate"]')
        self.note = (By.XPATH, '//button[@data-element="stickyToolGroupButton"]')
        self.page_container = (By.ID, 'pageContainer1')
        self.base_url = 'https://app.zipboard.co/storage/public/pdfPlayer'
        self.iframe = (By.ID, 'webviewer-1')
        self.note_text = (By.XPATH, '//div[contains(@class,"ql-editor")]/p')
        self.save_button = (By.XPATH, '//button[@class="save-button"]')
        self.saved_note = (By.XPATH, '//div[@class="Note"]')
        self.note_popup_button = (By.XPATH, '//div[@data-element="notePopup"]')
        self.note_popup_delete_button = (By.XPATH, '//button[@data-element="notePopupDelete"]')

    def get_annotate(self):
        return self.annotate

    def get_note(self):
        return self.note

    def get_page_container(self):
        return self.page_container

    def get_base_url(self):
        return self.base_url

    def get_iframe(self):
        return self.iframe

    def get_note_text(self):
        return self.note_text

    def get_save_button(self):
        return self.save_button

    def get_saved_note(self):
        return self.saved_note

    def get_note_popup_button(self):
        return self.note_popup_button

    def get_note_popup_delete_button(self):
        return self.note_popup_delete_button

    def click_annotate(self, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.get_annotate())).click()

    def click_note(self, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.get_note())).click()

    def click_save(self, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.get_save_button())).click()
        time.sleep(3)

    def click_page_container(self, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.get_page_container())).click()

    def click_saved_note(self, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.get_saved_note())).click()

    def click_note_popup(self, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.get_note_popup_button())).click()

    def click_note_popup_delete(self, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.get_note_popup_delete_button())).click()

    def switch_to_iframe(self, driver: webdriver.Chrome, wait: WebDriverWait):
        iframe = wait.until(EC.presence_of_element_located(self.get_iframe()))
        driver.switch_to.frame(iframe)

    def add_note_text(self, driver: webdriver.Chrome, wait: WebDriverWait, note: str):
        note_text_element = wait.until(EC.presence_of_element_located(self.get_note_text()))
        driver.execute_script("arguments[0].textContent = arguments[1];", note_text_element, note)
        time.sleep(3)

    def add_note_to_document(self, driver: webdriver.Chrome, wait: WebDriverWait, note: str):
        self.switch_to_iframe(driver, wait)
        self.click_annotate(wait)
        self.click_note(wait)
        self.click_page_container(wait)
        self.add_note_text(driver, wait, note)
        self.click_save(wait)
        driver.refresh()

    def delete_note(self, driver: webdriver.Chrome, wait: WebDriverWait):
        self.switch_to_iframe(driver, wait)
        self.click_saved_note(wait)
        self.click_note_popup(wait)
        self.click_note_popup_delete(wait)
