from selene import have, be, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_logo_display(setup_browser_1920_1080):

    browser.open('/')

    browser.element('.header__wrap_logo img').should(be.visible)

    browser.element('.header__wrap_logo img').should(have.attribute('alt').value('doctu.ru'))

    browser.element('.header__wrap_logo img').should(have.attribute('height').value('32'))

    browser.element('.header__wrap_logo img').should(have.attribute('width').value('124'))


def test_main_menu_elements(setup_browser_1920_1080):
    # Откройте главную страницу
    browser.open('/')

    # Выберите город
    all_citys_button = browser.element('[class="btn btn-white-green home-citys__all"]')
    all_citys_button.click()
    browser.all('.home-citys__list a .item__title').element_by(have.exact_text('Петрозаводск')).click()

    # Найдите элементы меню
    doctors_menu_item = browser.element(".main-menu__menu a[href='/petrozavodsk/doctors']")
    clinics_menu_item = browser.element(".main-menu__menu a[href='/petrozavodsk/clinics']")
    services_menu_item = browser.element(".main-menu__menu a[href='/petrozavodsk/services']")
    consultations_menu_item = browser.element(".main-menu__menu a[href='/consult']")

    # Проверьте наличие элементов меню
    doctors_menu_item.should(be.visible).should(have.exact_text('Врачи'))
    clinics_menu_item.should(be.visible).should(have.exact_text('Клиники'))
    services_menu_item.should(be.visible).should(have.exact_text('Услуги'))
    consultations_menu_item.should(be.visible).should(have.exact_text('Консультации'))

    # Кликните на каждый элемент и проверьте переход на соответствующую страницу
    doctors_menu_item.click()
    browser.should(have.url_containing('/petrozavodsk/doctors'))

    clinics_menu_item.click()
    browser.should(have.url_containing('/petrozavodsk/clinics'))

    services_menu_item.click()
    browser.should(have.url_containing('/petrozavodsk/services'))

    consultations_menu_item.click()
    browser.should(have.url_containing('/consult'))


def test_location_display_and_change(setup_browser_1920_1080):
    # Откройте главную страницу
    browser.open('/')

    # Найдите элемент местоположения
    current_location = browser.element('.header__wrap_placeanduser .header-place')

    # Проверьте, что текущее местоположение отображается
    current_location.should(have.exact_text('Петрозаводск'))

    # Симулируем изменение местоположения
    current_location.click()

    # Появляется попап с выбором города
    browser.element('.popup__wrap').should(be.visible)

    # Найдите список городов
    browser.all('.cities-list a').element_by(have.exact_text('Воронеж')).click()
    current_location.should(have.exact_text('Воронеж'))


def test_personal_cabinet_popup_display(setup_browser_1920_1080):
    # Откройте главную страницу
    browser.open('/')

    # Найдите ссылку на кнопку личный кабинет
    personal_cabinet_button = browser.element('.header-user-popup .header-user')

    # Проверьте, что кнопка личный кабинет видима
    personal_cabinet_button.should(be.visible)

    # Кликните на ссылку
    personal_cabinet_button.click()

    # Найдите ссылку на попап личный кабинет
    personal_cabinet_popup = browser.element('.popup__wrap')

    # Проверьте, что попап личный кабинет видимый
    personal_cabinet_popup.should(be.visible)


def test_burger_menu_visible(setup_browser_974_1080):
    # Откройте главную страницу
    browser.open('/')

    burger_menu = browser.element('.header__wrap_burger')

    burger_menu.should(be.visible)

def test_specialty_dropdown_visible_and_change(setup_browser_1920_1080):
    # Откройте главную страницу
    browser.open('/')

    # Проверьте, что поле выбора специальности врача отображается
    specialty_dropdown = browser.element('.vs__search')
    specialty_dropdown.should(be.visible)

    # Выберите специальность "хирург"
    specialty_dropdown.type('хирург')

    browser.element('.vs__dropdown-menu').element(by.text('Хирург')).click()

    # Проверьте, что выбранная специальность отображается в поле
    selected_specialty = browser.element('.vs__selected-options')
    selected_specialty.should(have.exact_text('Хирург'))


def test_search_button_visible(setup_browser_1920_1080):
    # Откройте главную страницу
    browser.open('/')

    # Проверьте, что кнопка "Найти" отображается на странице
    search_button = browser.element('.btn')

    # Проверьте, что кнопка "Найти" является видимой
    search_button.should(be.visible)


def test_check_correct_link_after_click_all_citys_button(setup_browser_1920_1080):
    # Шаг 1: Открыть главную страницу
    browser.open("/")

    # Шаг 2: Нажать на элемент <a> с текстом "Все города"
    all_citys_button = browser.element('[class="btn btn-white-green home-citys__all"]')
    all_citys_button.click()

    # Проверка: Убедиться, что текущий URL соответствует ожидаемому URL "/regions"
    browser.should(have.url('https://doctu.ru/regions'))


def test_check_text_on_all_citys_button(setup_browser_1920_1080):
    # Шаг 1: Открыть главную страницу
    browser.open("/")

    # Проверка: Убедиться, что текст элемента <a> равен "Все города"
    all_citys_button = browser.element('[class="btn btn-white-green home-citys__all"]')
    all_citys_button.should(have.exact_text('Все города'))