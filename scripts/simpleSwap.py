from brownie import GeneralSwap, Contract, accounts
from dotenv import load_dotenv

load_dotenv()
# aдреса для форка основной сети 
# WETHAddress = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
# DAIAddress = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
# адреса для sepolia
# WETHAddress = "0x7b79995e5f793A07Bc00c21412e50Ecae098E7f9"
# DAIAddress = "0x3e622317f8C93f7328350cF0B56d9eD4C620C5d6"

# адреса goerli
# tokenToAddress = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"
# tokenFromAddress = "0x9D233A907E065855D2A9c7d4B552ea27fB2E5a36"
WETHAddress = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"
swapRouterAddress = "0xE592427A0AEce92De3Edee1F18E0157C05861564"

def main():
    deployGeneralSwap(accounts[0])

def getToken(tokenAddress):
    return Contract.from_explorer(tokenAddress)

def getSymbol(_from, token):
    return token.symbol({
        'from': _from,
        'priority_fee': '10 wei'
    })

def deployGeneralSwap(_from, _tokenToAddress, _tokenFromAddress):
    deployed = GeneralSwap.deploy(swapRouterAddress, _tokenToAddress, _tokenFromAddress, {
        'from': _from,
        'priority_fee': '10 wei'
    }, publish_source=True)
    print(f'GeneralSwap successful deployed!')
    return deployed 

def wrapETH(_from, amount_gwei):
    weth = Contract.from_explorer(WETHAddress)
    weth.deposit({
        'from': _from,
        'value': f'{amount_gwei} gwei',
        'priority_fee': '10 wei'
    }).wait(1)
    print(f'{amount_gwei} successful wrapped!')

def balanceOf(_from, token):
    balance = token.balanceOf(_from, {
        'from': _from,
        'priority_fee': '10 wei'
    })
    print(f'Balance {getSymbol(_from, token)}: {balance}')
    return balance

def approve(_from, amount_gwei, tokenTo):
    tokenTo.approve(GeneralSwap[-1].address, f'{amount_gwei} gwei', {
        'from': _from,
        'priority_fee': '10 wei'
    })
    print(f'Approved GeneralSwap use {amount_gwei} gwei!')

def swapTokens(_from, amount):
    GeneralSwap[-1].swapTokens(amount, {
        'from': _from,
        'priority_fee': '2 gwei'
    }).wait(1)