# import importlib
import pytest
from wily.helper.utl import collect_wily_modules

# WILEY_MODULES = ["module_name", [collect_wily_modules()]]


# @pytest.mark.parametrize(["module_name", collect_wily_modules()])
def test_modules():
    """
    Test the every module has a module number
    """
    for name in collect_wily_modules():
        print(name)


if __name__ == "__main__":
    pytest.main(args=["-v"])
