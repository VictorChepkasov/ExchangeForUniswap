import pytest
from conftest import *
from scripts.helpful import getSymbol
from scripts.getQuote import deployQuoter, getQuote

@pytest.fixture(scope='session')
def quoter(user):
    return deployQuoter(user)

def test_gettingQuote(user, tokens, quoter, amount=10):
    tokenTo, tokenFrom = tokens
    print(f'Quote {getSymbol(user, tokenTo)} for {getSymbol(user, tokenFrom)}')
    amountOut = getQuote(user, tokenTo.address, tokenFrom.address, amount)
    assert isinstance(amountOut, int)