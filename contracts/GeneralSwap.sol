//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@uniswap/v3-periphery/contracts/interfaces/ISwapRouter.sol";
import "@uniswap/v3-periphery/contracts/libraries/TransferHelper.sol";

contract GeneralSwap {
    ISwapRouter public immutable swapRouter;
    address public tokenTo;
    address public tokenFrom;
    uint24 public constant feeTier = 3000;

    constructor(ISwapRouter _swapRouter, address _tokenTo, address _tokenFrom) {
        swapRouter = _swapRouter;
        tokenTo = _tokenTo;
        tokenFrom = _tokenFrom;
    }

    // amountIn in wei (1*10^18)
    function swapTokens(uint amountIn) external returns (uint256 amountOut) {
        // отправка токенов на этот контракт
        TransferHelper.safeTransferFrom(tokenTo, msg.sender, address(this), amountIn);
        // разрешение маршрутизатору тратить токены
        TransferHelper.safeApprove(tokenTo, address(swapRouter), amountIn);
        ISwapRouter.ExactInputSingleParams memory params = 
        ISwapRouter.ExactInputSingleParams({
            tokenIn: tokenTo,
            tokenOut: tokenFrom,
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