import dataclasses


@dataclasses.dataclass
class Users:
    full_name: str
    email: str
    address: str
    permanent_address: str


test_user = Users(
    full_name='Test testovich',
    email='test@mail.ru',
    address='Dom Pushkina boje kak je dolgo begayut testi na etom saite',
    permanent_address='kak je ya lyblu refactoring'
)
