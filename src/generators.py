from typing import Any, Dict, Generator, Iterator, List


def filter_by_currency(list_to_sort: List[Dict[str, Any]], currency_to_sort: str) -> Iterator:
    """
    Функция возвращает транзакцию по заданному значению ключа currency_to_sort
    """

    for transaction in list_to_sort:

        operation_amount = transaction["operationAmount"]

        currency = operation_amount["currency"]

        if currency["code"] == currency_to_sort:
            yield transaction


def transaction_descriptions(list_to_iteration: List[Dict[str, Any]]) -> Iterator:
    """
    Функция возвращает описание транзакции
    """

    for transaction in list_to_iteration:

        description = transaction["description"]

        yield description


def card_number_generator(start: int, end: int) -> Generator:
    """
    Функция генерирует номер карты в формате XXXX XXXX XXXX XXXX
    """

    if not (1 <= start):
        raise ValueError("Занижение начального значения 1")

    if not (end <= 9999999999999999):
        raise ValueError("Превышение конечного значения 9999999999999999")

    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")

    for number in range(start, end + 1):

        formatted_num = f"{number:016d}"

        num_generation = f"{formatted_num[:4]} {formatted_num[4:8]} {formatted_num[8:12]} {formatted_num[12:16]}"

        yield num_generation

        if num_generation == "9999 9999 9999 9999":
            break
