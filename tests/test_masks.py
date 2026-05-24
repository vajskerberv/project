import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_numbers, masked_card",
    [
        ("1234567887654321", "1234 56** **** 4321"),
        ("1234123412341234", "1234 12** **** 1234"),
        ("123456788765432", "Некорректный номер карты"),
        ("12341234123412341", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_numbers, masked_card):
    result = get_mask_card_number(int(card_numbers))
    expected = masked_card
    assert result == expected


@pytest.mark.parametrize(
    "account_numbers, masked_number",
    [
        ("1234567887654321", "**4321"),
        ("123456", "**3456"),
        ("12345", "**345"),
        ("1234", "**34"),
        ("123", "Некорректный номер счёта"),
    ],
)
def test_get_mask_account(account_numbers, masked_number):
    result = get_mask_account(int(account_numbers))
    expected = masked_number
    assert result == expected
