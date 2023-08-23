from brownie import GetQuote, Contract, accounts
from dotenv import load_dotenv

load_dotenv()

quoterAddress = "0x61fFE014bA17989E743c5F6cB21bF9697530B21e"

def main():
    deployQuoter(accounts[0])

def deployQuoter(_from):
    deployed = GetQuote.deploy(quoterAddress, {
        'from': _from,
        'priority_fee': '10 wei'
    }, publish_source=True)
    print('Quoter deployed successful!')
    return deployed

def getQuote(_from, tokenTo, tokenFrom, amountIn):
    amountOut = GetQuote[-1].getQuote.call(amountIn, tokenTo, tokenFrom, {
        'from': _from,
        'priority_fee': '10 wei'
    })
    print(f'Received quote: {amountOut}')
    return amountOut