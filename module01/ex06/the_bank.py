
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
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
        if key.find('b') != -1:
            delattr(corrupted_account, key)


class Bank(object):
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
        if amount < 0:
            return False

        if not isinstance(origin, int) and not isinstance(origin, str):
            return False

        if not isinstance(dest, int) and not isinstance(dest, str):
            return False

        for acc in self.account:
            if getattr(acc, "name") == origin or getattr(acc, "id") == origin:
                origin_bank_instance = acc
            elif getattr(acc, "name") == dest or getattr(acc, "id") == dest:
                dest_bank_instance = acc

        origin_class = dir(origin_bank_instance)
        dest_class = dir(dest_bank_instance)

        # print(origin_class, dest_class)

        # print(dest_bank_instance.name)
        # print(dest_bank_instance.id)
        # print(dest_bank_instance.value)
        #
        # print(origin_bank_instance.name)
        # print(origin_bank_instance.id)
        # print(origin_bank_instance.value)
        if len(origin_class) % 2 != 0 and len(dest_class) % 2 != 0:
            return False

        if has_attr_b(origin_class) or has_attr_b(dest_class):
            return False

        if not hasattr(origin_bank_instance, 'name'):
            return False

        if not hasattr(dest_bank_instance, 'name'):
            return False

        if not hasattr(origin_bank_instance, 'id'):
            return False

        if not hasattr(dest_bank_instance, 'id'):
            return False

        if not hasattr(origin_bank_instance, 'value'):
            return False

        if not hasattr(dest_bank_instance, 'value'):
            return False

        if (not isinstance(amount, float)) or amount < 0:
            return False
        origin_bank_instance.value -= amount
        dest_bank_instance.transfer(amount)
        return True

    def fix_account(self, account):
        """
        fix the corrupted account
        :param account: int(id) or str(name) of the account
        :return:    True if success, False is an error occured
        """
        if not (isinstance(account, int) and isinstance(account, str)):
            return False
        print(account)
        origin_bank = self.account[0]

        if has_attr_b(origin_bank):
            remove_attr(origin_bank)

        print(origin_bank.name)
        if not hasattr(origin_bank, 'value'):
            origin_bank.value = 0
        print(origin_bank.value)
        if not hasattr(origin_bank, 'zip'):
            origin_bank.zip = ""
        print(origin_bank.id)
        # Well I can' t Fix his name
        if not hasattr(origin_bank, 'name'):
            return False

        # Well I can' t Fix his id
        if not hasattr(origin_bank, 'id'):
            return False

        # Well 0 is no debt XD
        return True


