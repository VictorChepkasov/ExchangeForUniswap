from brownie import GeneralSwap
from dotenv import load_dotenv

load_dotenv()

swapRouterAddress = "0xE592427A0AEce92De3Edee1F18E0157C05861564"

def main():
    swapTokens()

def deployGeneralSwap(_from):
    deployed = GeneralSwap.deploy(swapRouterAddress, {
        'from': _from,
        'priority_fee': '10 wei'
    }, publish_source=True)
    print('GeneralSwap successful deployed!')
    return deployed 

def swapTokens(_from, amount, tokenTo, tokenFrom):
    GeneralSwap[-1].swapTokens(amount, tokenTo, tokenFrom, {
        'from': _from,
        'priority_fee': '2 gwei'
    }).wait(1)