import pytest
from brownie import accounts, network
from scripts.simpleSwap import (
    deploySimpleSwap,
    wrapETH,
    DAIBalance,
    approve,
    swapTokens
)

@pytest.fixture(scope='session')
def user():
    if network.show_active() != 'development':
        return accounts.load('victor')
    else:
        return accounts[0]

@pytest.fixture
def simpleSwap(user):
    return deploySimpleSwap(user)

def test_swap(user, simpleSwap, amount=10):
    # connect to WETH and wrap some eth
    wrapETH(user, amount+1)
    # get DAI balance
    DAIBalanceBefore = DAIBalance(user)
    # approve
    approve(user, amount)
    # swap tokens
    swapTokens(user, amount-2)
    DAIBalanceAfter = DAIBalance(user)
    assert DAIBalanceBefore < DAIBalanceAfter