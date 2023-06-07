import pytest

from inifile import IniData
from inifile import IniFile


def test():
    cfg = IniFile("hello.ini")
    assert cfg["foo.value"] == "42"


def test_IniData_len():
    data = IniData({"a": "aval"})
    assert len(data) == 1
    data["a"] += "more"
    assert sum(1 for _ in data) == 1
    assert len(data) == 1
    data["b"] = "bval"
    assert len(data) == 2
    del data["a"]
    assert len(data) == 1
    del data["b"]
    assert len(data) == 0
