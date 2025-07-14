from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email: str = None
    current_address: str = None
    mobile: str = None
    subject: str = None

    # def __init__(self, first_name):
        # self.first_name = dfirst_name
        # self.url = url
        # use decorator instead

