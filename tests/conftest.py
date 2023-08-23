import pytest
from brownie import accounts, network
from scripts.helpful import getToken

# aдреса для основной сети 
# WETHAddress = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
# DAIAddress = "0x6B175474E89094C44Da98b954EedeAC495271d0F"

# адреса goerli
# tokenToAddress = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"
# tokenFromAddress = "0x9D233A907E065855D2A9c7d4B552ea27fB2E5a36"

@pytest.fixture(scope='session')
def user():
    if network.show_active() != 'development':
        return accounts.load('victor')
    else:
        return accounts[0]
    
@pytest.fixture(scope='session')
def tokens():
    tokenTo = getToken("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6")
    tokenFrom = getToken("0x9D233A907E065855D2A9c7d4B552ea27fB2E5a36")
    return tokenTo, tokenFrom
