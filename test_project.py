from project import get_bank, get_deposit, get_withdraw, ask_transaction

def main():
    test_get_bank()
    test_get_deposit()
    test_get_withdraw()
    test_ask_transaction()

def test_get_bank():
    assert get_bank("cHAse") == "chase"
    assert get_bank("WELLS FARGO") == "wells fargo"
    assert get_bank("U.s BaNk") == "u.s bank"
    assert get_bank("citi bank") == "citi bank"

def test_get_deposit():
    assert get_deposit("-45") == "Invalid Amount"
    assert get_deposit("-75.47") == "Invalid Amount"
    assert get_deposit("45.42") == "45.42"
    assert get_deposit("0") == "0"
    assert get_deposit("any characters") == "Invalid Amount"

def test_get_withdraw():
    assert get_withdraw("-45") == "Invalid Amount"
    assert get_withdraw("-75.47") == "Invalid Amount"
    assert get_withdraw("45.42") == "45.42"
    assert get_withdraw("0") == "0"
    assert get_withdraw("any characters") == "Invalid Amount"

def test_ask_transaction():
    assert ask_transaction("YES") == "yes"
    assert ask_transaction("yes") == "yes"
    assert ask_transaction("Y") == "yes"
    assert ask_transaction("y") == "yes"
    assert ask_transaction("NO") == "no"
    assert ask_transaction("no") == "no"
    assert ask_transaction("N") == "no"
    assert ask_transaction("n") == "no"

