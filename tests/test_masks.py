import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_numbers, masked_card",
    [
        (1234567887654321, "1234 56** **** 4321"),
        (1234123412341234, "1234 12** **** 1234"),
        (123456788765432, "Некорректный номер карты"),
        (12341234123412341, "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_numbers: int, masked_card: str) -> None:
    result = get_mask_card_number(card_numbers)
    expected = masked_card
    assert result == expected


def test_get_mask_card_number_with_fixture(mask_card_number: str) -> None:
    assert get_mask_card_number(4856294728553957) == mask_card_number


@pytest.mark.parametrize(
    "account_numbers, masked_number",
    [
        (1234567887654321, "**4321"),
        (123456, "**3456"),
        (12345, "**345"),
        (1234, "**34"),
        (123, "Некорректный номер счёта"),
    ],
)
def test_get_mask_account(account_numbers: int, masked_number: str) -> None:
    result = get_mask_account(account_numbers)
    expected = masked_number
    assert result == expected
