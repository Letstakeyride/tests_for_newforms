import dataclasses
import datetime
from enum import Enum


class UserGender(Enum):
    Male = 1
    Female = 2
    Other = 3


class UserHobby(Enum):
    Sports = 1
    Reading = 2
    Music = 3


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: UserGender
    phone: str
    date_of_birth: datetime.date
    subject: str
    hobby: UserHobby
    picture: str
    address: str
    state: str
    city: str


test_user = Users(
    first_name="User",
    last_name="Test",
    email="test@mail.ru",
    gender=UserGender.Male,
    phone="8800055535",
    date_of_birth=datetime.date(1998, 6, 15),
    subject="Commerce",
    hobby=UserHobby.Music,
    picture="test.jpg",
    address="Dom Pushkina boje kak je dolgo begayut testi na etom saite",
    state="NCR",
    city="Gurgaon",
)
