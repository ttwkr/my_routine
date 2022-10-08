import string, random, os


class Common:
    def __init__(self):
        self._NUMBER = string.digits

    def rand_number_code(self, length: int = 6):
        random.seed = (os.urandom(1024))
        return ''.join(random.choice(str(self._NUMBER)) for _ in range(length))
