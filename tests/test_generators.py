from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency_code, expected_count", [("USD", 3), ("RUB", 2)])
def test_filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str, expected_count: int) -> None:
    result = list(filter_by_currency(transactions, currency_code))
    assert len(result) == expected_count


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод организации"},
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        )
    ],
)
def test_transaction_descriptions(transactions: List[Dict[str, Any]], expected_descriptions: str) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (5, 5, ["0000 0000 0000 0005"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected
