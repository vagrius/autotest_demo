from selenium.webdriver.common.by import By


class YandexBasePageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGESTIONS_LIST = (By.CSS_SELECTOR, ".mini-suggest__popup-content")
    RESULTS_LIST = (By.CSS_SELECTOR, "#search-result .serp-item .Link_theme_outer")
    IMAGES_LINK = (By.CSS_SELECTOR, "[data-id='images']")
    FIRST_CATEGORY_LINK = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 .PopularRequestList-Preview")
    FIRST_CATEGORY_SEARCH_TEXT = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 .PopularRequestList-SearchText")
    SEARCH_FIELD_IMAGES = (By.CSS_SELECTOR, ".input__control")
    FIRST_IMAGE_LINK = (By.CSS_SELECTOR, ".serp-item_pos_0 .serp-item__link")
    FIRST_IMAGE_DESCRIPTION = (By.CSS_SELECTOR, ".serp-item_pos_0 .serp-item__thumb.justifier__thumb")
    IMAGE_VIEWER = (By.CSS_SELECTOR, ".MediaViewer-LayoutMain")
    IMAGE_CONTAINER = (By.CSS_SELECTOR, "body")
    IMAGE_SELECTED = (By.CSS_SELECTOR, ".MMGallery-Item_selected .MMThumbImage-Image")
