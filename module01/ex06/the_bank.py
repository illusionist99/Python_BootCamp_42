
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        :param origin: int(id) or str(name) of the first account
        :param dest:  int(id) or str(name) of the destination account
        :param amount: float(amount) amount to transfer
        :return: True if success, False is an error occured
        """
        if not isinstance(self, Bank):
            return False

        if not (isinstance(origin, int) and isinstance(origin, str)):
            return False

        if not (isinstance(dest, int) and isinstance(dest, str)):
            return False

        if (not isinstance(amount, float)) or amount < 0:
            return False
        if Account(origin).value != amount:
            return False
        else:
            Account(origin).value -= amount
            Account(dest).value += amount

        return True

    def fix_account(self, amount):
        """
        fix the corrupted account
        :param amount: int(id) or str(name) of the account
        :return:    True if success, False is an error occured
        """
        if not (isinstance(amount, int) and isinstance(amount, str)):
            return False

        return True



x = Account("name")
print(dir(x))