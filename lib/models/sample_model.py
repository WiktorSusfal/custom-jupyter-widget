import random
import string

class SampleModel:
    """
    Sample model class exposing two attributes.
    """

    def __init__(self):
        self.var_1, self.var_2 = self._generate_data()

    def _generate_data(self) -> tuple[str, int]:
        return self.generate_random_string(10), random.randint(0, 9)

    def generate_random_string(self, length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def __repr__(self):
        return self.var_1 + ', ' + str(self.var_2)