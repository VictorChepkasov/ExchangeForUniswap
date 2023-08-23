import pytest
from conftest import *
from scripts.helpful import (
    getSymbol,
    wrapETH,
    balanceOf,
    approve
)
from scripts.generalSwap import (
    deployGeneralSwap,
    swapTokens
)

@pytest.fixture(scope='session')
def generalSwap(user, tokens):
    print(f'Swap {getSymbol(user, tokens[0])} for {getSymbol(user, tokens[1])}')
    return deployGeneralSwap(user, tokens[0].address, tokens[1].address)

def test_swap(user, generalSwap, tokens, amount=10):
    tokenTo, tokenFrom = tokens
    # connect to WETH and wrap some eth
    wrapETH(user, amount+1)
    # get DAI balance
    DAIBalanceBefore = balanceOf(user, tokenFrom)
    # approve
    approve(user, amount, tokenTo)
    # swap tokens
    swapTokens(user, amount-2)
    DAIBalanceAfter = balanceOf(user, tokenFrom)
    assert DAIBalanceBefore < DAIBalanceAfter