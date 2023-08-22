//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@uniswap/v3-periphery/contracts/interfaces/ISwapRouter.sol";
import "@uniswap/v3-periphery/contracts/libraries/TransferHelper.sol";

contract SimpleSwap {
    ISwapRouter public immutable swapRouter;
    // 1inch = 0x111111111117dC0aa78b770fA6A738034120C302 
    address public constant DAI = 0x9D233A907E065855D2A9c7d4B552ea27fB2E5a36;
    address public constant WETH9 = 0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6;
    uint24 public constant feeTier = 3000;

    constructor(ISwapRouter _swapRouter) {
        swapRouter = _swapRouter;
    }

    // amountIn in wei (1*10^18)
    function swapWETHForDAI(uint amountIn) external returns (uint256 amountOut) {
        // отправка токенов на этот контракт
        TransferHelper.safeTransferFrom(WETH9, msg.sender, address(this), amountIn);
        // разрешение маршрутизатору тратить токены
        TransferHelper.safeApprove(WETH9, address(swapRouter), amountIn);
        ISwapRouter.ExactInputSingleParams memory params = 
        ISwapRouter.ExactInputSingleParams({
            tokenIn: WETH9,
            tokenOut: DAI,
            fee: feeTier,
            recipient: msg.sender,
            deadline: block.timestamp,
            amountIn: amountIn,
            // по сути позволяет вам установить минимальную сумму вывода, в данном случае DAI, которую вы получите за своп. В продакшне это один из способов ограничить проскальзывание цены от свопа
            amountOutMinimum: 0,
            sqrtPriceLimitX96: 0
        });
        // выполнение обмена
        amountOut = swapRouter.exactInputSingle(params);
        return amountOut;
    }
}