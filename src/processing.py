def filter_by_state(list_to_sort_by_state: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает отсортированный список коллекций по ключу state
    """

    sorted_list = []

    for key in list_to_sort_by_state:
        if key.get("state") == state:
            sorted_list.append(key)
        else:
            continue

    return sorted_list


def sort_by_date(list_to_sort_by_date: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция возвращает список коллекций отсортированный по дате. По умолчанию - убывание
    """
    return sorted(list_to_sort_by_date, key=lambda x: x["date"], reverse=reverse)
