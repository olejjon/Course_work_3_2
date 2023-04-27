import json
from datetime import datetime
import re


# Чтение с сортировкой списка по убыванию даты
def sort_json():
    with open('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = sorted(data, key=lambda x: x.get("date", ""), reverse=True)
    return data


# Нормализация даты под условия задачи
def date_normal(date):
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


# Функция скрытия номера карты и замены
def hide_number(from_transfer):
    match = re.search(r"\d{12,19}", from_transfer)
    if not match:
        # Если номер карты не найден, возвращаем исходный текст без изменений
        return from_transfer
    else:
        card_number = match.group()
        masked_card_number = mask_card_number(card_number)

        masked_text = from_transfer.replace(card_number, masked_card_number)
        return masked_text


def mask_card_number(match):
    # Извлечение первых 6 и последних 4 цифр из номера карты
    first_six = match[:6]
    last_four = match[-4:]

    # Замена всех цифр между первыми 6 и последними 4 на символы *
    len_star = "*" * (len(match) - len(first_six) - len(last_four))

    new_number_card = first_six + len_star + last_four

    split_number = [new_number_card[i:i + 4] for i in range(0, len(new_number_card), 4)]
    return ' '.join(split_number)


def card_account(to_transfer):
    match = re.search(r"\d{12,20}", to_transfer)
    # match_letter = re.search(r"\b([A-Za-z]+)\b", to_transfer)
    if not match:
        # Если номер карты не найден, возвращаем исходный текст без изменений
        return to_transfer
    else:
        return 'Счет ' + '*' * 2 + match.group()[-4:]
