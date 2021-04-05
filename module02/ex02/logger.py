import time
from random import randint

# @log is just an easier way of saying a = log(func)


def log(func):

    def wrapper(*args):
        f = open("machine.log", "a")
        start_time = time.time()
        if callable(func):
            func(*args)
        f.write(f'(cmaxime)Running: {func.__name__:<8} [ exec-time = {func.__name__} ]\n')
        f.close()
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        print("Please add water!")
        return False

    @log
    def boil_water(self):
        print("boiling...")

    @log
    def make_coffee(self):
        if not self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            self.boil_water()
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
