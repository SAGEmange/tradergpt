import { calculateProfit } from '../utils/tradeUtils.js';

export const analyzeTradeImage = (req, res) => {
  const { entry = 0, exit = 0, shares = 0 } = req.body;
  const profit = calculateProfit(entry, exit, shares);

  res.json({
    analysis: {
      trend: 'bullish',
      confidence: 0.85,
    },
    profit,
  });
};
