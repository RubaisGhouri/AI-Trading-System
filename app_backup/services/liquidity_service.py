"""
QuantNova Liquidity Detection Engine
"""

from app.services.technical_service import TechnicalService


class LiquidityService:

    @classmethod
    def analyze(cls):

        tech = TechnicalService.analyze()

        candles = tech["candles"]

        highs = candles["high"].tolist()

        lows = candles["low"].tolist()

        closes = candles["close"].tolist()

        tolerance = 0.0015

        equal_high = False
        equal_low = False

        buy_side_liquidity = None
        sell_side_liquidity = None

        liquidity_sweep = "NONE"

        # ==========================
        # Equal High
        # ==========================

        for i in range(len(highs)-15, len(highs)-1):

            for j in range(i+1, len(highs)):

                if abs(highs[i]-highs[j])/highs[i] < tolerance:

                    equal_high = True

                    buy_side_liquidity = round(max(highs[i], highs[j]),2)

        # ==========================
        # Equal Low
        # ==========================

        for i in range(len(lows)-15, len(lows)-1):

            for j in range(i+1, len(lows)):

                if abs(lows[i]-lows[j])/lows[i] < tolerance:

                    equal_low = True

                    sell_side_liquidity = round(min(lows[i], lows[j]),2)

        # ==========================
        # Sweep Detection
        # ==========================

        last_close = closes[-1]

        last_high = highs[-1]

        last_low = lows[-1]

        if buy_side_liquidity:

            if last_high > buy_side_liquidity and last_close < buy_side_liquidity:

                liquidity_sweep = "BUY SIDE SWEEP"

        if sell_side_liquidity:

            if last_low < sell_side_liquidity and last_close > sell_side_liquidity:

                liquidity_sweep = "SELL SIDE SWEEP"

        return {

            "equal_high": equal_high,

            "equal_low": equal_low,

            "buy_side_liquidity": buy_side_liquidity,

            "sell_side_liquidity": sell_side_liquidity,

            "liquidity_sweep": liquidity_sweep

        }