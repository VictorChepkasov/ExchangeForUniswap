import pytest
from brownie import accounts, network
from scripts.simpleSwap import (
    deploySimpleSwap,
    wrapETH,
    balanceOf,
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
def tokens():
    tokenTo = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"
    tokenFrom = "0x9D233A907E065855D2A9c7d4B552ea27fB2E5a36"
    return tokenTo, tokenFrom

@pytest.fixture
def simpleSwap(user, tokens):
    return deploySimpleSwap(user, tokens[0], tokens[1])

def test_swap(user, simpleSwap, tokens, amount=10):
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