"""
Market Analysis Agent.
"""

from agents.base_agent import BaseAgent


class MarketAgent(BaseAgent):
    """
    AI agent specialized in market analysis.
    """

    @property
    def agent_name(self) -> str:
        return "MarketAgent"

    def analyze(
        self,
        symbol: str,
        timeframe: str,
        market_data: str | None = None,
    ):
        """
        Analyze a trading symbol.
        """

        prompt = f"""
Analyze the following market.

Symbol:
{symbol}

Timeframe:
{timeframe}
"""

        if market_data:
            prompt += f"""

Market Data:
{market_data}
"""

        prompt += """

Provide:

1. Market Trend
2. Support Levels
3. Resistance Levels
4. Market Structure
5. Trading Bias
6. Entry Idea
7. Stop Loss
8. Take Profit
9. Risk Level

Be concise and professional.
"""

        return self.ask(prompt)