from typing import Union


class SimpleDomainName:
    def __init__(self, fqdn: Union[str, None] = None):
        self.fqdn = fqdn
        parts = fqdn.split('.')
        self.tld = parts[-1]
        self.domain = parts[-2]
        self.subdomains = parts[:-2]

    def __str__(self):
        return self.fqdn

    def __repr__(self):
        return f"{self.__class__.__name__}({self.fqdn})"


class URL:
    pass


if __name__ == '__main__':
    test = SimpleDomainName('test.example.com')
    print(test.subdomains)  # Output: ['test']
