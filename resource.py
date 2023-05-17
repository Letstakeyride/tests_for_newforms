from imghdr import tests
from pathlib import Path

file_name = 'test.jpg'


def path(file_name):
    return str((Path().joinpath(f'resources/{file_name}').absolute()))


['Student Name', 'User Test', 'Student Email', 'test@mail.ru', 'Gender', 'Male', 'Mobile', '8800055535',
 'Date of Birth', '15 June,1998', 'Subjects', 'Commerce', 'Hobbies', 'Reading', 'Picture', 'test.jpg', 'Address',
 'Dom Pushkina boje kak je dolgo begayut testi na etom saite', 'State and City', 'NCR Gurgaon']

("Student Name", "User Test"),
("Student Email", "test@mail.ru"),
("Gender", "Male"),
("Mobile", "8800055535"),
("Date of Birth", "15 June,1998"),
("Subjects", "Commerce"),
("Hobbies", "Reading"),
("Picture", "test.jpg"),
("Address", "Dom Pushkina boje kak je dolgo begayut testi na etom saite"),
("State and City", "NCR Gurgaon"),