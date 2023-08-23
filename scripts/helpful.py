from brownie import GeneralSwap, Contract

WETHAddress = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"

def getToken(tokenAddress):
    return Contract.from_explorer(tokenAddress)

def getSymbol(_from, token):
    return token.symbol({
        'from': _from,
        'priority_fee': '10 wei'
    })

def wrapETH(_from, amount_gwei):
    weth = Contract.from_explorer(WETHAddress)
    weth.deposit({
        'from': _from,
        'value': f'{amount_gwei} gwei',
        'priority_fee': '10 wei'
    }).wait(1)
    print(f'{amount_gwei} ethers successful wrapped!')

def balanceOf(_from, token):
    balance = token.balanceOf(_from, {
        'from': _from,
        'priority_fee': '10 wei'
    })
    print(f'Balance {getSymbol(_from, token)}: {balance}')
    return balance

def approve(_from, amountGwei, tokenTo):
    tokenTo.approve(GeneralSwap[-1].address, f'{amountGwei} gwei', {
        'from': _from,
        'priority_fee': '10 wei'
    })
    print(f'Approved GeneralSwap use {amountGwei} gwei!')