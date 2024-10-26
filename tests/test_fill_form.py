from pages.registration_page import RegistrationPage
import allure
from path_config import RESOURCES_PATH
import pytest

@pytest.mark.smoke
@allure.tag('web')
@allure.label("owner", 'zakharovaaa')
@allure.feature('Форма регистрации студента')
@allure.story('Заполнения всех полей')
@allure.title('Заполнить все поля на форме')
@allure.suite('Проверка формы регистрации')
def test_fill_form():
    registration_page = RegistrationPage()

    with allure.step('Открыть страницу формы'):
        registration_page.open('/automation-practice-form')

    with allure.step('Заполнить форму'):
        registration_page.fill_first_name('Анастасия')
        registration_page.fill_last_name('З')
        registration_page.fill_user_email('test@mail.ru')
        registration_page.fill_female()
        registration_page.fill_user_number('7927000000')
        registration_page.fill_date_of_birth(20, 6, 1995)
        registration_page.fill_subjects('Arts')
        registration_page.fill_hobbies()
        registration_page.fill_picture(RESOURCES_PATH)
        registration_page.fill_current_address('Samara')
        registration_page.fill_state_and_city()
        registration_page.submit_button()

    with allure.step('Проверить корректность заполнения формы'):
        registration_page.should_registered_user_with(
            'Анастасия З',
            'test@mail.ru',
            'Female',
            '7927000000',
            '20 July,1995',
            'Arts',
            'Music',
            'image.jpg',
            'Samara',
            'Haryana Karnal')
