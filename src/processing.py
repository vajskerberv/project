def filter_by_state(list_: list, state: str = 'EXECUTED') -> list:
    sorted_list = []
    for key in list_:
        if key.get('state') == state:
            sorted_list.append(key)
        else:
            continue
    return sorted_list
