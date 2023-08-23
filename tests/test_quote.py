import pytest
from conftest import *
# from brownie import 
from scripts.helpful import getSymbol
from scripts.getQuote import deployQuoter, getQuote

@pytest.fixture(scope='session')
def quoter(user, tokens):
    print(f'Received quote: {getSymbol(user, tokens[0])} for {getSymbol(user, tokens[1])}')
    return deployQuoter(user, tokens[0].address, tokens[1].address)

def test_gettingQuote():
    pass