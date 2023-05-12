from selene.support.shared import browser
import os
from selene import have


def test_registration_with_valid_data():
    browser.open("/automation-practice-form")

    browser.element("#firstName").type("User")
    browser.element("#lastName").type("Test")
    browser.element("#userEmail").type("test@mail.ru")
    browser.element('[value="Male"] + label').click()
    browser.element("#userNumber").type("8800055535")

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.all(".react-datepicker__month-select option").element_by(have.exact_text("June")).click()
    browser.element(".react-datepicker__year-select").click()
    browser.all(".react-datepicker__year-select option").element_by(have.exact_text("1998")).click()
    browser.all(".react-datepicker__day").element_by(have.exact_text("15")).click()

    browser.element("#subjectsInput").type("Commerce").press_enter()
    browser.all("[for^=hobbies]").element_by(have.exact_text("Reading")).click()
    browser.element("#uploadPicture").type(f"{os.getcwd()}/test.png")

    browser.element("#currentAddress").type("Dom Pushkina boje kak je dolgo begayut testi na etom saite")
    browser.element("#state").click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element("#city").click()
    browser.all("#city div").element_by(have.exact_text("Gurgaon")).click()

    browser.element("#submit").press_enter()

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
