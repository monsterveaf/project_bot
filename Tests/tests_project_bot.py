from unittest import TestCase

from Main import get_weather
from Main import weather_token


class TestProjectBot(TestCase):
    def test_get_weather(self) -> None:
        """This test checks whether input from a user equals output from API"""
        cases = [
            ("Moscow", ("Moscow", weather_token)),
            ("Saint Petersburg", ("Saint Petersburg", weather_token)),
            ("Tver'", ("Tver'", weather_token)),
            ("Perm", ("Perm", weather_token)),
            ("Samara Oblast", ("Samara Oblast", weather_token))
        ]
        for k, v in cases:
            with self.subTest(k):
                self.assertEqual(k.lower(), get_weather(*v)["Your location"].lower())
