
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


def has_attr_b(lst):
    for key in lst:
        if 'b' == key[0]:
            return True
    return False


def remove_attr(corrupted_account):
    lst = dir(corrupted_account)
    for key in lst:
        if 'b' == key[0]:
            delattr(corrupted_account, key)



class Bank:
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        if not isinstance(account, Account):
            exit("Bank class Can't accept instances of Account only")
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

        origin_class = dir(origin)
        dest_class = dir(dest)

        if len(origin_class) % 2 != 0 or len(dest_class) % 2 != 0:
            return False

        if has_attr_b(origin_class) or has_attr_b(dest_class):
            return False

        if not hasattr(self, 'name'):
            return False

        if not hasattr(self, 'id'):
            return False

        if hasattr(self, 'value'):
            return False

        if (not isinstance(amount, float)) or amount < 0:
            return False
        if Account(origin).value != amount:
            return False
        else:
            Account(origin).value -= amount
            Account(dest).value += amount
        return True




    # noinspection PyMethodMayBeStatic
    def fix_account(self, account):
        """
        fix the corrupted account
        :param account: int(id) or str(name) of the account
        :return:    True if success, False is an error occured
        """
        if not (isinstance(account, int) and isinstance(account, str)):
            return False
        corrupted_account = Account(account)
        account_class = dir(corrupted_account)
        if has_attr_b(account_class):
            remove_attr(corrupted_account)

        if not hasattr(self, 'name'):
            return False

        if not hasattr(self, 'id'):
            return False

        if hasattr(self, 'value'):
            return False
        return True


x = Account("name")
print(dir(x))
