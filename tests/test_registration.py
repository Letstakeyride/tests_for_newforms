from selene.support.shared import browser
from selene import have

from models.pages.registration_page import RegistrationPage
from resources import resource


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open()

    # browser.element("#firstName").type("User")
    registration_page.fill_first_name('User')
    # browser.element("#lastName").type("Test")
    registration_page.fill_last_name('Test')
    # browser.element("#userEmail").type("test@mail.ru")
    registration_page.fill_email('test@mail.ru')
    # browser.element('[value="Male"] + label').click()
    registration_page.choose_gender('Male')
    # browser.element("#userNumber").type("8800055535")
    registration_page.add_mobile_phone('8800055535')
    # browser.element("#dateOfBirthInput").click()
    # browser.element(".react-datepicker__month-select").click()
    # browser.all(".react-datepicker__month-select option").element_by(have.exact_text("June")).click()
    # browser.element(".react-datepicker__year-select").click()
    # browser.all(".react-datepicker__year-select option").element_by(have.exact_text("1998")).click()
    # browser.all(".react-datepicker__day").element_by(have.exact_text("15")).click()
    registration_page.fill_date_of_birth('1998', 'June', '15')

    # browser.element("#subjectsInput").type("Commerce").press_enter()
    registration_page.fill_subject('Commerce')
    # browser.all("[for^=hobbies]").element_by(have.exact_text("Reading")).click()
    registration_page.choose_hobbies('Reading')
    # browser.element('#uploadPicture').set_value(resource.path('test.png'))
    registration_page.upload_photo('test.png')
    # browser.element("#currentAddress").type("Dom Pushkina boje kak je dolgo begayut testi na etom saite")
    registration_page.fill_state('Dom Pushkina boje kak je dolgo begayut testi na etom saite')
    # browser.element("#state").click()
    # browser.all("#state div").element_by(have.exact_text("NCR")).click()
    # browser.element("#city").click()
    # browser.all("#city div").element_by(have.exact_text("Gurgaon")).click()
    registration_page.choose_state_and_city('NCR', 'Gurgaon')
    # browser.element("#submit").press_enter()
    registration_page.submit()
    browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
    browser.all(".table").all("td").should(
        have.exact_texts(
            ("Student Name", "User Test"),
            ("Student Email", "test@mail.ru"),
            ("Gender", "Male"),
            ("Mobile", "8800055535"),
            ("Date of Birth", "15 June,1998"),
            ("Subjects", "Commerce"),
            ("Hobbies", "Reading"),
            ("Picture", "test.png"),
            ("Address", "Dom Pushkina boje kak je dolgo begayut testi na etom saite"),
            ("State and City", "NCR Gurgaon"),
        )
    )
