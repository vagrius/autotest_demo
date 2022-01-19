from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .locators import YandexBasePageLocators
import time


class YandexBasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_page_opened(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_search_field(self):
        assert self.is_element_present(*YandexBasePageLocators.SEARCH_FIELD), "Search field is not presented"

    def should_be_suggestions_list(self):
        search_field = self.browser.find_element(*YandexBasePageLocators.SEARCH_FIELD)
        search_field.send_keys('тензор')
        time.sleep(3)
        assert self.is_element_present(*YandexBasePageLocators.SUGGESTIONS_LIST), "Suggestions list is not presented"

    def should_be_search_results(self):
        search_field = self.browser.find_element(*YandexBasePageLocators.SEARCH_FIELD)
        search_field.send_keys('тензор')
        search_field.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        results = self.browser.find_elements(*YandexBasePageLocators.RESULTS_LIST)
        count = 0
        for result in results[:6]:
            if result.get_attribute('href').find('tensor.ru') != -1:
                count += 1
        assert count == 5, f"tensor.ru is in {count} results of 5"

    def should_be_images_link(self):
        assert self.is_element_present(*YandexBasePageLocators.IMAGES_LINK), "Pictures link is not presented"

    def go_to_images_page(self):
        link = self.browser.find_element(*YandexBasePageLocators.IMAGES_LINK)
        link.click()
        self.browser.implicitly_wait(5)

    def is_images_page_opened(self):
        original_window = self.browser.current_window_handle
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break
        assert self.browser.current_url.find('https://yandex.ru/images') != -1, "Wrong page opened"

    def go_to_first_images_category_page(self):
        link = self.browser.find_element(*YandexBasePageLocators.FIRST_CATEGORY_LINK)
        text = self.browser.find_element(*YandexBasePageLocators.FIRST_CATEGORY_SEARCH_TEXT).text
        link.click()
        self.browser.implicitly_wait(3)
        return text

    def is_search_text_correct(self, text):
        time.sleep(3)
        assert self.browser.title.find(text) != -1, "Text in search input is not correct"

    def go_to_first_image_page(self):
        link = self.browser.find_element(*YandexBasePageLocators.FIRST_IMAGE_LINK)
        self.browser.find_element(*YandexBasePageLocators.FIRST_IMAGE_DESCRIPTION).get_attribute('alt')
        link.click()
        self.browser.implicitly_wait(3)

    def is_search_image_page_opened(self):
        assert self.is_page_opened(*YandexBasePageLocators.IMAGE_VIEWER), "Image has not be opened"

    def is_image_changing_when_press_arrow_right(self):
        initial_image = self.browser.find_element(*YandexBasePageLocators.IMAGE_SELECTED).get_attribute('style')
        container = self.browser.find_element(*YandexBasePageLocators.IMAGE_CONTAINER)
        container.send_keys(Keys.ARROW_RIGHT)
        time.sleep(3)
        assert self.browser.find_element(*YandexBasePageLocators.IMAGE_SELECTED).get_attribute('style') != \
               initial_image, "Image has not change"
        return initial_image

    def is_image_changing_when_press_arrow_left(self, initial_image):
        container = self.browser.find_element(*YandexBasePageLocators.IMAGE_CONTAINER)
        container.send_keys(Keys.ARROW_LEFT)
        time.sleep(3)
        assert self.browser.find_element(*YandexBasePageLocators.IMAGE_SELECTED).get_attribute('style') == \
               initial_image, "Image has not change or this is not initial image"
