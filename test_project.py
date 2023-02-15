import pytest
import project
import csv

def test_get_option(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4")
    with pytest.raises(ValueError):
        project.get_option()

    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert project.get_option() == "2"

def test_sell():
    assert project.sell("KES", 1) == 0
    assert project.sell("notacurrency", 1) == 1

def test_convert():
    assert round(project.convert("UGX"), 1) == round(1 / project.convert("UGX", inverse=True), 1)
    assert round(project.convert("GBP"), 1) == round(1 / project.convert("GBP", inverse=True), 1)
    



