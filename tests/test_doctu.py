import allure
from selene import have, be, by
from selene.support.shared import browser

@allure.title('Checking the logo display')
def test_logo_display(setup_browser_1920_1080):
    with allure.step('Open home page'):
        browser.open('/')

    with allure.step('Make sure the logo is displayed'):
        browser.element('.header__wrap_logo img').should(be.visible)
    with allure.step('Check that the logo contains the correct link to the image'):
        browser.element('.header__wrap_logo img').should(have.attribute('src').value('https://doctu.ru/img/logo.svg'))
    with allure.step('Check that the image height is 32px'):
        browser.element('.header__wrap_logo img').should(have.attribute('height').value('32'))
    with allure.step('Check that the image width is 124px'):
        browser.element('.header__wrap_logo img').should(have.attribute('width').value('124'))


@allure.title('Check the operation of the "All cityes" button')
def test_all_cityes_button(setup_browser_1920_1080):
    with allure.step('Open home page'):
        browser.open('/')

    with allure.step('Click on the "All cities" button'):
        all_cities_button = browser.element('[class="btn btn-white-green home-citys__all"]')
        all_cities_button.click()
    with allure.step('Check that the transition to the desired page occurs'):
        browser.should(have.url_containing('/regions'))
    with allure.step('Select a city Petrozavodsk from the list'):
        browser.all('.home-citys__list a .item__title').element_by(have.exact_text('Петрозаводск')).click()

    with allure.step('Check that the city of Petrozavodsk is selected'):
        city_in_header = browser.element('.header-place')
        city_in_header.should(have.exact_text('Петрозаводск'))


@allure.title('Check the main menu in the header')
def test_main_menu_elements(setup_browser_1920_1080):
    with allure.step('Open home page'):
        browser.open('/')

    with allure.step('Select a city Petrozavodsk'):
        all_citys_button = browser.element('[class="btn btn-white-green home-citys__all"]')
        all_citys_button.click()
        browser.all('.home-citys__list a .item__title').element_by(have.exact_text('Петрозаводск')).click()

    with allure.step('Check the visibility of the "Doctors" element'):
        doctors_menu_item = browser.element(".main-menu__menu a[href='/petrozavodsk/doctors']")
        doctors_menu_item.should(be.visible)
    with allure.step('Check that the "Doctors" element contains the correct text'):
        doctors_menu_item.should(have.exact_text('Врачи'))
    with allure.step('Check that when you click on the “Doctors” element, you go to the corresponding page'):
        doctors_menu_item.click()
        browser.should(have.url_containing('/petrozavodsk/doctors'))

    with allure.step('Check the visibility of the "Clinics" element'):
        clinics_menu_item = browser.element(".main-menu__menu a[href='/petrozavodsk/clinics']")
        clinics_menu_item.should(be.visible)
    with allure.step('Check that the "Clinics" element contains the correct text'):
        clinics_menu_item.should(have.exact_text('Клиники'))
    with allure.step('Check that when you click on the “Clinics” element, you go to the corresponding page'):
        clinics_menu_item.click()
        browser.should(have.url_containing('/petrozavodsk/clinics'))

    with allure.step('Check the visibility of the "Services" element'):
        services_menu_item = browser.element(".main-menu__menu a[href='/petrozavodsk/services']")
        services_menu_item.should(be.visible)
    with allure.step('Check that the "Services" element contains the correct text'):
        services_menu_item.should(have.exact_text('Услуги'))
    with allure.step('Check that when you click on the “Services” element, you go to the corresponding page'):
        services_menu_item.click()
        browser.should(have.url_containing('/petrozavodsk/services'))

    with allure.step('Check the visibility of the "Services" element'):
        consultations_menu_item = browser.element(".main-menu__menu a[href='/consult']")
        consultations_menu_item.should(be.visible)
    with allure.step('Check that the "Services" element contains the correct text'):
        consultations_menu_item.should(have.exact_text('Консультации'))
    with allure.step('Check that when you click on the “Services” element, you go to the corresponding page'):
        consultations_menu_item.click()
        browser.should(have.url_containing('/consult'))


@allure.title('Check the change of home city using the current location button in the header')
def test_location_display_and_change(setup_browser_1920_1080):
    with allure.step('Open home page'):
        browser.open('/')

    with allure.step(('Check that your current location is displayed')):
        current_location = browser.element('.header__wrap_placeanduser .header-place')
        current_location.should(be.visible)
    with allure.step('Click on the current location button'):
        current_location.click()
    with allure.step('Check the appearance of a pop-up with a city selection'):
        browser.element('.popup__wrap').should(be.visible)

    with allure.step('Change current location to Voronezh'):
        browser.all('.cities-list a').element_by(have.exact_text('Воронеж')).click()
        current_location.should(have.exact_text('Воронеж'))


@allure.title('Check the opening of the "Personal Account" popup using the personal account button')
def test_personal_cabinet_popup_display(setup_browser_1920_1080):
    with allure.step('Open home page'):
        browser.open('/')

    with allure.step('Check that the personal account button is visible'):
        personal_cabinet_button = browser.element('.header-user-popup .header-user')
        personal_cabinet_button.should(be.visible)
    with allure.step('Click on the personal account button'):
        personal_cabinet_button.click()

    with allure.step('Check that the "Personal Account" popup is visible'):
        personal_cabinet_popup = browser.element('.popup__wrap')
        personal_cabinet_popup.should(be.visible)


@allure.title('Check burger menu display')
def test_burger_menu_visible(setup_browser_960_1080):
    with allure.step('Open home page'):
        browser.open('/')
    with allure.step('Check that the burger menu is visible'):
        burger_menu = browser.element('.header__wrap_burger')
        burger_menu.should(be.visible)
    with allure.step('Click on the burger menu'):
        burger_menu.click()
    with allure.step('Check that the menu expands'):
        mobile_menu = browser.element(".main-menu__wrap")
        mobile_menu.should(be.visible)


@allure.title("Checking the search string for doctor's specialty")
def test_specialty_dropdown_visible_and_change(setup_browser_1920_1080):
    with allure.step('Open home page'):
        browser.open('/')

    with allure.step("Field for selecting a doctor's specialty is visible"):
        specialty_dropdown = browser.element('.vs__search')
        specialty_dropdown.should(be.visible)

    with allure.step('Type "surgeon" in the specialty selection field'):
        specialty_dropdown.type('хирург')

    with allure.step('Click on the "Surgeon" line'):
        browser.element('.vs__dropdown-menu').element(by.text('Хирург')).click()

    with allure.step('Check that the selected specialty is displayed in the specialty selection field'):
        selected_specialty = browser.element('.vs__selected-options')
        selected_specialty.should(have.exact_text('Хирург'))


@allure.title('Check that the "Find" button is visible and contains the correct text')
def test_search_button_visible(setup_browser_1920_1080):
    with allure.step('Open home page'):
        browser.open('/')

    with allure.step('Check that the “Find” button is visible'):
        search_button = browser.element('.btn')
        search_button.should(be.visible)

    with allure.step('Check that the "Find" button contains text "Найти"'):
        search_button.should(have.exact_text('Найти'))


def test_check_cities_in_list(setup_browser_1920_1080):
    # Шаг 1: Открыть главную страницу
    browser.open("/")

    # Проверка наличия всех нужных названий городов
    expected_cities = ['Москва', 'Санкт-Петербург', 'Волгоград', 'Воронеж', 'Екатеринбург', 'Казань', 'Краснодар',
                     'Красноярск', 'Нижний Новгород', 'Новосибирск', 'Омск', 'Пермь', 'Ростов-на-Дону', 'Самара', 'Уфа',
                     'Челябинск']


def test_check_text_on_all_citys_button(setup_browser_1920_1080):
    # Шаг 1: Открыть главную страницу
    browser.open("/")

    # Проверка: Убедиться, что текст элемента <a> равен "Все города"
    all_citys_button = browser.element('[class="btn btn-white-green home-citys__all"]')
    all_citys_button.should(have.exact_text('Все города'))