"""
Miscelaionus utility methods for wily

MODULE:0-5
"""
import pathlib


class WilyModules(object):

    WILEY_ROOT = pathlib.Path(__file__).joinpath("..").resolve()

    def __init__(self):
        self._all_modules = None
