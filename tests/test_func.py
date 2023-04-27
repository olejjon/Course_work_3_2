import funcs


def test_date_normal():
    assert funcs.date_normal("2019-12-03T04:27:03.427014") == "03.12.2019"
    assert funcs.date_normal("2019-08-04T20:17:25.443322") == "04.08.2019"
    assert funcs.date_normal("2019-09-07T07:20:13.889610") == "07.09.2019"


def test_hide_number():
    assert funcs.hide_number("Maestro 4284341727554246") == "Maestro 4284 34** **** 4246"
    assert funcs.hide_number("Visa Classic 4040551273087672") == "Visa Classic 4040 55** **** 7672"
    assert funcs.hide_number("Счет 65298957349197687907") == "Счет 6529 89** **** ***8 7907"


def test_card_account():
    assert funcs.card_account("Счет 38784565940893479418") == "Счет **9418"
    assert funcs.card_account("Visa Gold 2684274847577419") == "Счет **7419"
    assert funcs.card_account("Visa Platinum 7825450883088021") == "Счет **8021"

