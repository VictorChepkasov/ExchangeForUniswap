import pytest
from conftest import *
from scripts.generalSwap import deployGeneralSwap, swapTokens
from scripts.helpful import (
    getSymbol,
    wrapETH,
    balanceOf,
    approve
)

@pytest.fixture(scope='session')
def generalSwap(user):
    return deployGeneralSwap(user)

def test_swap(user, generalSwap, tokens, amount=10):
    tokenTo, tokenFrom = tokens
    print(f'Swap {getSymbol(user, tokenTo)} for {getSymbol(user, tokenFrom)}')
    # connect to WETH and wrap some eth
    wrapETH(user, amount+1)
    # get DAI balance
    DAIBalanceBefore = balanceOf(user, tokenFrom)
    # approve
    approve(user, amount, tokenTo)
    # swap tokens
    swapTokens(user, amount-2, tokenTo.address, tokenFrom.address)
    DAIBalanceAfter = balanceOf(user, tokenFrom)
    assert DAIBalanceBefore < DAIBalanceAfter