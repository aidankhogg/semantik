from typing import Union

from commons.definitions.datatipes.technical import SimpleDomainName


class EmailAddress:
    def __init__(self, address: Union[str, None] = None):
        try:
            self.mailbox, self.domain = address.split('@')
            self.domain = SimpleDomainName(self.domain)

        except ValueError as err:
            print(f"Error: {err}")
            self.mailbox = None
            self.domain = None
        except AttributeError as err:
            print(f"Error: {err}")
            self.mailbox = None
            self.domain = None

    def __str__(self):
        return f"{self.mailbox}@{self.domain}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__str__()})"

    def __eq__(self, other):
        return self.mailbox == other.mailbox and self.domain == other.domain

    def __ne__(self, other):
        return not self.__eq__(other)

    def set(self,
            full_address: Union[str, None] = None,
            mailbox: Union[str, None] = None,
            domain: Union[str, None, SimpleDomainName] = None):
        if full_address:
            self.mailbox, self.domain = full_address.split('@')
        else:
            if mailbox:
                self.mailbox = mailbox
            else:
                raise ValueError("Mailbox cannot be None")
            if domain:
                self.domain = SimpleDomainName(domain)
            else:
                raise ValueError("Domain cannot be None")

    def is_valid(self):
        raise NotImplementedError("This method is not implemented yet")


class PhoneNumber:
    raise NotImplementedError("This class is not implemented yet")


class AddressLine:
    pass


class City(AddressLine):
    pass


class State(AddressLine):
    pass


class Country(AddressLine):
    pass


class PostalCode(AddressLine):
    pass


class Address:
    def __init__(self):
        self.streets: list[AddressLine] = []
        self.city: City = City()
        self.state: State = State()
        self.country: Country = Country()
        self.postal_code: PostalCode = PostalCode()

    def to_dict(self):
        return {
            "streets": self.streets,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "postal_code": self.postal_code
        }

    def to_str(self):
        return f"{self.streets}, {self.city}, {self.state}, {self.country}, {self.postal_code}"

    def __str__(self):
        return self.to_str()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_str()})"
