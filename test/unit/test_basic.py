# import importlib
import pytest
from wily.helper.utl import collect_wily_modules

WILEY_MODULES = ["module_name", [collect_wily_modules()]]


@pytest.mark.parametrize(WILEY_MODULES)
def test_modules(module_name):
    """
    Test the every module has a module number
    """
    print(module_name)


if __name__ == "__main__":
    pytest.main(args=["-v"])
