import pathlib
from pkgutil import iter_modules
from setuptools import find_packages
# import pytest

WILY_ROOT = pathlib.Path("wily").resolve()
print(WILY_ROOT)

def get_all_modules():
    wily_modules = set()
    for pkg in find_packages():
        pkg_path = f"{WILY_ROOT.parent}/{pkg.replace('.', '/')}"
        print(pkg_path, pkg)
        for _, name, ispkg in iter_modules([pkg_path]):
            if ispkg:
                pass
            else:
                # print("added", name)
                wily_modules.add(f"{pkg}.{name}")
    return wily_modules

if __name__ == "__main__":
    print(get_all_modules())
