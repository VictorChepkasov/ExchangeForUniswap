//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@uniswap/v3-periphery/contracts/interfaces/IQuoterV2.sol";

contract GetQuote {
    IQuoterV2 public immutable quoter;
    address public tokenTo;
    address public tokenFrom;
    uint24 public constant feeTier = 3000;

    constructor(IQuoterV2 _quoter, address _tokenTo, address _tokenFrom) {
        quoter = _quoter;
        tokenTo = _tokenTo;
        tokenFrom = _tokenFrom;
    }

    function getQuote(uint amountIn) external returns(uint amountOut) {
        IQuoterV2.QuoteExactInputSingleParams memory params = IQuoterV2.QuoteExactInputSingleParams({
            tokenIn: tokenTo,
            tokenOut: tokenFrom,
            amountIn: amountIn,
            fee: feeTier,
            sqrtPriceLimitX96: 0
        });
        // получение котировок
        (amountOut,,,) = quoter.quoteExactInputSingle(params);
        return amountOut;
    }
}