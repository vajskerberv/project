# Импорт функий маскировки номера карты и номера счёта
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция принимает номер карты или счёта и возвращает замаскированный номер
    """

    part_name = account_card.split()

    number = int(part_name[-1])

    name_and_number = " ".join(part_name[:-1])

    if name_and_number.lower() == "счет":
        masked_number = get_mask_account((number))
    else:
        masked_number = get_mask_card_number((number))

    return f"{name_and_number} {masked_number}"


def get_date(iso_format: str) -> str:
    """
    Функция принимает дату в формате ГГГГ-ММ-ДДТЧЧ:ММ:СС
    и возвращает ДД.ММ.ГГГГ
    """
    modified_data = iso_format[8:10] + "." + iso_format[5:7] + "." + iso_format[0:4]
    return modified_data
