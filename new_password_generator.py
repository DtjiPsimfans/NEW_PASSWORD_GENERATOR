import random
from datetime import date
import pickle
import sys


class WebStorage:
    """
    This class contains attributes of the storage of the web.
    """

    def __init__(self):
        # type: () -> None
        self.start: date = date.today()
        self.time_password_modified: date = date.today()
        self.today: date = date.today()
        self.password: str = self.generate_password()

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += "Date Web Storage Started: " + str(self.start.day) + "/" + str(self.start.month) + "/" + \
               str(self.start.year) + "\n"
        res += "Date Password Modified: " + str(self.start.day) + "/" + str(self.start.month) + "/" + \
               str(self.start.year) + "\n"
        res += "Today's Date: " + str(self.start.day) + "/" + str(self.start.month) + "/" + \
               str(self.start.year) + "\n"
        res += "Password: " + str(self.password) + "\n"
        return res

    def update_time(self):
        # type: () -> None
        self.today = date.today()

    def generate_password(self):
        # type: () -> str
        self.password = ""  # initial value
        # If the web storage has just been started
        if self.start == self.time_password_modified == self.today:
            # Generating a new password
            self.add_random_characters_to_password()

        return self.password

    def add_random_characters_to_password(self):
        # type: () -> None
        num_characters: int = random.randint(1, 50) if len(self.password) >= 15 else random.randint(15, 50)
        POSSIBLE_CHARS: str = " _abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*()[]{}|/~`"
        for i in range(num_characters):
            # Adding a random character to the password
            self.password += str(POSSIBLE_CHARS[random.randint(0, len(POSSIBLE_CHARS) - 1)])

    def change_password(self):
        # type: () -> bool
        # If the password has existed for one month
        if (self.today - self.time_password_modified).days == 30:
            initial_password: str = self.password
            self.password = ""  # initial value
            # Changing the password to a new password
            self.add_random_characters_to_password()
            # Ensuring that the new password is not the same as the old password
            while self.password == initial_password:
                self.password = ""
                self.add_random_characters_to_password()

            self.time_password_modified = date.today()
            self.update_time()
            return True
        return False


def main():
    # type: () -> None
    """
    This function is used to run the program
    :return:
    """

    web_storage: WebStorage
    filename: str = "Saved Web Storage Data"
    try:
        web_storage = pickle.load(open(filename, "rb"))
    except FileNotFoundError:
        web_storage = WebStorage()

    web_storage.update_time()
    web_storage.change_password()
    print(web_storage)
    pickle.dump(web_storage, open(filename, "wb"))
    sys.exit()


if __name__ == '__main__':
    main()
