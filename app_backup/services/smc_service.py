"""
QuantNova Smart Money Concepts Engine
Uses Shared MarketDataService
"""

from app.services.market_data_service import MarketDataService


class SMCService:

    @classmethod
    def analyze(
        cls,
        symbol="BTCUSDT",
        interval="1h",
        limit=300,
    ):

        df = MarketDataService.get_dataframe(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        swing_highs = []
        swing_lows = []

        for i in range(2, len(df)-2):

            if (
                df["high"][i] > df["high"][i-1]
                and df["high"][i] > df["high"][i-2]
                and df["high"][i] > df["high"][i+1]
                and df["high"][i] > df["high"][i+2]
            ):
                swing_highs.append(df["high"][i])

            if (
                df["low"][i] < df["low"][i-1]
                and df["low"][i] < df["low"][i-2]
                and df["low"][i] < df["low"][i+1]
                and df["low"][i] < df["low"][i+2]
            ):
                swing_lows.append(df["low"][i])

        price = float(df["close"].iloc[-1])

        last_high = swing_highs[-1] if swing_highs else None
        prev_high = swing_highs[-2] if len(swing_highs) >= 2 else None

        last_low = swing_lows[-1] if swing_lows else None
        prev_low = swing_lows[-2] if len(swing_lows) >= 2 else None

        bos = "NO BOS"

        if last_high and price > last_high:
            bos = "BULLISH BOS"

        elif last_low and price < last_low:
            bos = "BEARISH BOS"

        choch = "NO CHOCH"

        if prev_high and last_high:

            if last_high < prev_high:
                choch = "BEARISH CHOCH"

        if prev_low and last_low:

            if last_low > prev_low:
                choch = "BULLISH CHOCH"

        structure = "RANGE"

        if bos == "BULLISH BOS":
            structure = "UPTREND"

        elif bos == "BEARISH BOS":
            structure = "DOWNTREND"

        elif choch != "NO CHOCH":
            structure = "REVERSAL"

        return {

            "price": round(price,2),

            "last_swing_high": round(last_high,2) if last_high else None,

            "last_swing_low": round(last_low,2) if last_low else None,

            "bos": bos,

            "choch": choch,

            "market_structure": structure,

            "swing_high_count": len(swing_highs),

            "swing_low_count": len(swing_lows)

        }