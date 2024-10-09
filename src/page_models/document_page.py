import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


class DocumentPage:

    def __init__(self):
        self.annotate: tuple[str, str] = (By.XPATH, '//button[@data-element="toolbarGroup-Annotate"]')
        self.shapes: tuple[str, str] = (By.XPATH, '//button[@data-element="toolbarGroup-Shapes"]')
        self.note: tuple[str, str] = (By.XPATH, '//button[@data-element="stickyToolGroupButton"]')
        self.line: tuple[str, str] = (By.XPATH, '//button[@data-element="lineToolGroupButton"]')
        self.page_container: tuple[str, str] = (By.ID, 'pageContainer1')
        self.base_url: str = 'https://app.zipboard.co/storage/public/pdfPlayer'
        self.iframe: tuple[str, str] = (By.ID, 'webviewer-1')
        self.note_text: tuple[str, str] = (By.XPATH, '//div[contains(@class,"ql-editor")]/p')
        self.save_button: tuple[str, str] = (By.XPATH, '//button[@class="save-button"]')
        self.saved_note: tuple[str, str] = (By.XPATH, '//div[@class="Note"]')
        self.note_popup_button: tuple[str, str] = (By.XPATH, '//div[@data-element="notePopup"]')
        self.note_popup_delete_button: tuple[str, str] = (By.XPATH, '//button[@data-element="notePopupDelete"]')
        self.canvas: tuple[str, str] = (By.XPATH, '//canvas[@class="auxiliary"]')
        self.cancel_button: tuple[str, str] = (By.XPATH, '//button[@class="cancel-button"]')

    def get_annotate(self) -> tuple[str, str]:
        return self.annotate

    def get_shapes(self) -> tuple[str, str]:
        return self.shapes

    def get_note(self) -> tuple[str, str]:
        return self.note

    def get_line(self) -> tuple[str, str]:
        return self.line

    def get_page_container(self) -> tuple[str, str]:
        return self.page_container

    def get_base_url(self) -> str:
        return self.base_url

    def get_iframe(self) -> tuple[str, str]:
        return self.iframe

    def get_note_text(self) -> tuple[str, str]:
        return self.note_text

    def get_save_button(self) -> tuple[str, str]:
        return self.save_button

    def get_saved_note(self) -> tuple[str, str]:
        return self.saved_note

    def get_note_popup_button(self) -> tuple[str, str]:
        return self.note_popup_button

    def get_note_popup_delete_button(self) -> tuple[str, str]:
        return self.note_popup_delete_button

    def get_canvas(self) -> tuple[str, str]:
        return self.canvas

    def get_cancel_button(self) -> tuple[str, str]:
        return self.cancel_button

    def click_annotate(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_annotate())).click()

    def click_shapes(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_shapes())).click()

    def click_note(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_note())).click()

    def click_line(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_line())).click()

    def click_save(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_save_button())).click()
        time.sleep(3)

    def click_page_container(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_page_container())).click()

    def click_saved_note(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_saved_note())).click()

    def click_note_popup(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_note_popup_button())).click()

    def click_note_popup_delete(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_note_popup_delete_button())).click()

    def click_cancel_button(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_cancel_button())).click()

    def switch_to_iframe(self, driver: webdriver.Chrome, wait: WebDriverWait) -> None:
        iframe: WebElement = wait.until(EC.presence_of_element_located(self.get_iframe()))
        driver.switch_to.frame(iframe)

    def switch_to_last_tab(self, driver: webdriver.Chrome) -> None:
        driver.switch_to.window(driver.window_handles[-1])

    def add_note_text(self, driver: webdriver.Chrome, wait: WebDriverWait, note: str) -> None:
        note_text_element: WebElement = wait.until(EC.presence_of_element_located(self.get_note_text()))
        driver.execute_script("arguments[0].textContent = arguments[1];", note_text_element, note)
        time.sleep(3)

    def draw_line_on_canvas(self, driver: webdriver.Chrome, wait: WebDriverWait) -> None:
        canvas: WebElement = wait.until(EC.presence_of_element_located(self.get_canvas()))
        action: ActionChains = ActionChains(driver)
        action.move_to_element_with_offset(canvas, 50, 50).click_and_hold()
        action.move_by_offset(150, 50).release().perform()

    def add_note_to_document(self, driver: webdriver.Chrome, wait: WebDriverWait, note: str) -> bool:
        try:
            self.switch_to_iframe(driver, wait)
            self.click_annotate(wait)
            self.click_note(wait)
            self.click_page_container(wait)
            self.add_note_text(driver, wait, note)
            self.click_save(wait)
        except:
            driver.refresh()
            return False
        driver.refresh()
        return True

    def delete_note(self, driver: webdriver.Chrome, wait: WebDriverWait) -> None:
        self.switch_to_iframe(driver, wait)
        self.click_saved_note(wait)
        self.click_note_popup(wait)
        self.click_note_popup_delete(wait)
        self.switch_to_last_tab(driver)

    def add_line_to_document(self, driver: webdriver.Chrome, wait: WebDriverWait) -> bool:
        try:
            self.switch_to_iframe(driver, wait)
            self.click_shapes(wait)
            self.click_line(wait)
            self.draw_line_on_canvas(driver, wait)
            self.click_page_container(wait)
        except:
            driver.refresh()
            return False
        time.sleep(3)
        driver.refresh()
        return True

    def delete_line(self, driver: webdriver.Chrome, wait: WebDriverWait) -> None:
        self.switch_to_iframe(driver, wait)
        self.click_saved_note(wait)
        self.click_cancel_button(wait)
        self.click_note_popup(wait)
        self.click_note_popup_delete(wait)
