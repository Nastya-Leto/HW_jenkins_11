from selene import browser, be, have


class RegistrationPage:
    def open(self, value):
        browser.open(value)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def fill_female(self):
        browser.element('[value=Female]').double_click()

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').element(f'[value = "{month}"]').click()
        browser.element('.react-datepicker__year-select').element(f'[value = "{year}"]').click()
        browser.element('.react-datepicker__month').element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_tab()

    def fill_hobbies(self):
        browser.element('label[for="hobbies-checkbox-3"]').click()

    def fill_picture(self, value):
        browser.element('#uploadPicture').send_keys(value)

    def fill_current_address(self, value):
        browser.element("[placeholder='Current Address']").type(value)

    def fill_state_and_city(self):
        browser.element('#state').click().element('#react-select-3-option-2').click()
        browser.element('#city').click().element('#react-select-4-option-0').click()

    def submit_button(self):
        browser.element('#submit').click()

    def should_registered_user_with(self, full_name, email, female, number, birthday, subjects, hobbies,
                                    file_name_download,
                                    address, state):
        browser.element('.modal-content').element('table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                female,
                number,
                birthday,
                subjects,
                hobbies,
                file_name_download,
                address,
                state))
