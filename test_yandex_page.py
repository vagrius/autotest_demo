from .pages.yandex_main_page import YandexMainPage
from .pages.yandex_images_page import YandexImagesPage


YANDEX_MAIN_PAGE_LINK = "https://yandex.ru/"
YANDEX_IMAGES_PAGE_LINK = "https://yandex.ru/images/"


class TestYandexSearch:

    def test_search_field(self, browser):
        page = YandexMainPage(browser, YANDEX_MAIN_PAGE_LINK)
        page.open()
        page.should_be_search_field()  # проверяем наличие поля поиска
        page.should_be_suggestions_list()  # проверяем, появилась ли таблица с подсказками

    def test_search_results(self, browser):
        page = YandexMainPage(browser, YANDEX_MAIN_PAGE_LINK)
        page.open()
        page.should_be_search_results()  # проверяем, есть ли в первых 5 результатах tensor.ru


class TestYandexPictures:

    def test_yandex_images_links(self, browser):
        page = YandexMainPage(browser, YANDEX_MAIN_PAGE_LINK)
        page.open()
        page.should_be_images_link()  # проверяем, есть ли ссылка "Картинки"
        page.go_to_images_page()
        page.is_images_page_opened()  # проверяем, что перешли на https://yandex.ru/images/

    def test_yandex_pictures_page(self, browser):
        page = YandexImagesPage(browser, YANDEX_IMAGES_PAGE_LINK)
        page.open()
        search_text = page.go_to_first_images_category_page()  # переходим на страницу категории и получаем ее текст
        # далее проверяем, что текст верный - по факту этого сделать нельзя, т.к. в html значение в инпуте нигде не
        # отображается, поэтому в качестве обходного решения проверяем по заголовку; это же проверка того, что открыли
        # нужную страницу
        page.is_search_text_correct(search_text)
        description = page.go_to_first_image_page()  # переходим на страницу первой картинки
        page.is_search_image_page_opened(description)  # проверяем, что страница открылась
