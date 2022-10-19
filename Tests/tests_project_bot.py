from unittest import TestCase

from Main import get_weather
from Main import weather_token
from Main import dict_return


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

    def test_dict_return(self) -> None:
        """This func test the correct output of dict_return"""

        cases = [
            (["2: 1\n" "3: 1\n"], {"2": "1", "3": "1"}),
            (["word: something\n" "nothing: goodjob\n"], {"word": "something", "nothing": "goodjob"}),
            (["temp: 42C\n" "wind: 53m/s\n" "humidity: 76%\n"], {"temp": "42C", "wind": "53m/s", "humidity": "76%"}),
        ]

        for k, v in cases:
            with self.subTest(k):
                self.assertEqual(*k, dict_return(v))
