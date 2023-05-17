from selene import have, command
from selene.support.shared import browser

import resource
from data.users import Users


class RegistrationPage:

    def __init__(self, user: Users):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.element(f'[value="{user.gender.name}"] + label')
        self.phone = browser.element("#userNumber")
        self.subject = browser.element("#subjectsInput")
        self.hobby = browser.all("[for^=hobbies]").element_by(have.exact_text(f"{user.hobby.name}"))
        self.address = browser.element("#currentAddress")

    def open(self):
        browser.open("/automation-practice-form")
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.all('#footer').perform(command.js.remove)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def upload_photo(self, picture):
        browser.element('#uploadPicture').set_value(resource.path(picture))
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

    def register(self, user: Users):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.click()
        self.phone.type(user.phone)
        self.fill_date_of_birth(
            user.date_of_birth.strftime("%Y"),
            user.date_of_birth.strftime("%B"),
            user.date_of_birth.strftime("%d"),
        )
        self.subject.type(user.subject).press_enter()
        self.hobby.click()
        self.upload_photo(user.picture)
        self.address.type(user.address)
        self.choose_state_and_city(user.state, user.city)
        self.submit()

    def should_have_registered(self, user: Users):
        browser.all(".table").all("td").should(
            have.exact_texts(
                ("Student Name", f'{user.first_name} {user.last_name}'),
                ("Student Email", user.email),
                ("Gender", user.gender.name),
                ("Mobile", user.phone),
                ("Date of Birth", user.date_of_birth.strftime('%d %B,%Y')),
                ("Subjects", user.subject),
                ("Hobbies", user.hobby.name),
                ("Picture", user.picture),
                ("Address", user.address),
                ("State and City", f'{user.state} {user.city}'),
            )
        )
