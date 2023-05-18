import os
from imghdr import tests

from selene import have, command
from selene.support.shared import browser

import resource


class RegistrationPage:
    def __int__(self):
        pass

    def open(self):
        browser.open("/automation-practice-form")
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.all('#footer').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def choose_gender(self, value):
        browser.element(f'[value={value}] + label').click()
        return self

    def add_mobile_phone(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()
        return self

    def choose_hobbies(self, value):
        browser.all("[for^=hobbies]").element_by(have.exact_text(value)).click()
        return self

    def upload_photo(self, picture):
        project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        resources_path = os.path.join(project_root_path, "tests", "resources")
        browser.element("#uploadPicture").type(f"{resources_path}/{picture}")
        return self

    def fill_state(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def choose_state_and_city(self, state, city):
        browser.element("#state").click()
        browser.all("#state div").element_by(have.exact_text(state)).click()
        browser.element("#city").click()
        browser.all("#city div").element_by(have.exact_text(city)).click()
        return self

    def submit(self):
        browser.element("#submit").press_enter()
        return self

    def should_have(
            self,
            full_name,
            email,
            gender,
            phone,
            birthday,
            subject,
            hobby,
            picture,
            address,
            state_and_city,
    ):
        browser.all(".table").all("td").should(
            have.exact_texts(
                ("Student Name", full_name),
                ("Student Email", email),
                ("Gender", gender),
                ("Mobile", phone),
                ("Date of Birth", birthday),
                ("Subjects", subject),
                ("Hobbies", hobby),
                ("Picture", picture),
                ("Address", address),
                ("State and City", state_and_city),
            )
        )
