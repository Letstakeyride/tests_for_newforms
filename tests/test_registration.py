from selene.support.shared import browser
from selene import have

from models.pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('User')

    registration_page.fill_last_name('Test')

    registration_page.fill_email('test@mail.ru')

    registration_page.choose_gender('Male')

    registration_page.add_mobile_phone('8800055535')

    registration_page.fill_date_of_birth('1998', 'June', '15')

    registration_page.fill_subject('Commerce')

    registration_page.choose_hobbies('Reading')

    registration_page.upload_photo('test.jpg')

    registration_page.fill_state('Dom Pushkina boje kak je dolgo begayut testi na etom saite')

    registration_page.choose_state_and_city('NCR', 'Gurgaon')

    registration_page.submit()
    registration_page.should_have(
        'User Test',
        'test@mail.ru',
        'Male',
        '8800055535',
        '15 June,1998',
        'Commerce',
        'Reading',
        'test.jpg',
        'Dom Pushkina boje kak je dolgo begayut testi na etom saite',
        'NCR Gurgaon',
    )
