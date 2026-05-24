import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected_masking_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 700079228960636", "Visa Platinum Некорректный номер карты"),
        ("Visa Platinum 70007922896063611", "Visa Platinum Некорректный номер карты"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Maestro 700079228960636", "Maestro Некорректный номер карты"),
        ("Maestro 70007922896063611", "Maestro Некорректный номер карты"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 736541", "Счет **6541"),
        ("Счет 73654", "Счет **654"),
        ("Счет 7365", "Счет **65"),
        ("Счет 736", "Счет Некорректный номер счёта"),
    ],
)
def test_mask_account_card(account_card, expected_masking_result):
    result = mask_account_card(account_card)
    expected = expected_masking_result
    assert result == expected


@pytest.mark.parametrize(
    "iso_date, expected_result",
    [
        ("2000-01-01T00:00:00", "01.01.2000"),
        ("2017-07-26T14:26:36", "26.07.2017"),
        ("2023-10-15T16:43:15", "15.10.2023"),
    ],
)
def test_get_date(iso_date, expected_result):
    result = get_date(iso_date)
    expected = expected_result
    assert result == expected
