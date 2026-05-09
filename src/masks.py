def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты
    и маскирует в формате ХХХХ ХХ** **** ХХХХ
    """
    card_str = str(card_number)
    if len(card_str) > 16 or len(card_str) < 16:
        return "Некорректный номер карты"
    elif len(card_str) == 16:
        masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        return masked


def get_mask_account(account_number: int) -> str:
    """Функция принимает номер счета
    и маскирует в формате **ХХХХ
    """
    account_str = str(account_number)
    if len(account_str) < 4:
        return "Некорректный номер счёта"
    elif len(account_str) == 4:
        last_four_digits = account_str[-2:]
        return f"**{last_four_digits}"
    elif len(account_str) == 5:
        last_four_digits = account_str[-3:]
        return f"**{last_four_digits}"
    elif len(account_str) > 5:
        last_four_digits = account_str[-4:]
        return f"**{last_four_digits}"
