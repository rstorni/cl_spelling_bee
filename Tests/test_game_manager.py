import pytest
from Source import game_manager as gm


class TestManager:

    def setup_method(self, method):
        print(f'Setting up {method}')
        self.sm = gm.Manager(['list', 'hats', 'felt'])

    def test_get_playing_initial(self):
        assert self.sm.get_playing() is True

    def test_get_playing_after_setting(self):
        self.sm.set_playing(False)
        assert self.sm.get_playing() is False

    def test_rand_letters(self):
        letters = self.sm.rand_letters(3, 4)
        assert len(letters) == 7  # Assuming you always want a total of 7 letters
        assert isinstance(letters, list)
