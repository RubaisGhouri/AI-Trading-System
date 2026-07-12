"""
QuantNova Institutional Confluence Engine
"""

from app.services.technical_service import TechnicalService
from app.services.support_resistance_service import SupportResistanceService
from app.services.multi_timeframe_service import MultiTimeframeService
from app.services.smc_service import SMCService
from app.services.order_block_service import OrderBlockService
from app.services.fvg_service import FVGService


class ConfluenceService:

    @classmethod
    def analyze(cls):

        technical = TechnicalService.analyze()

        sr = SupportResistanceService.analyze()

        mtf = MultiTimeframeService.analyze()

        smc = SMCService.analyze()

        ob = OrderBlockService.analyze()

        fvg = FVGService.analyze()

        score = 0

        reasons = []

        # =====================================
        # Trend
        # =====================================

        if technical["trend"] == "BULLISH":

            score += 20
            reasons.append("Bullish Trend")

        elif technical["trend"] == "BEARISH":

            score -= 20
            reasons.append("Bearish Trend")

        # =====================================
        # RSI
        # =====================================

        if technical["rsi"] < 35:

            score += 10
            reasons.append("Oversold RSI")

        elif technical["rsi"] > 70:

            score -= 10
            reasons.append("Overbought RSI")

        # =====================================
        # MACD
        # =====================================

        if technical["macd_cross"]:

            score += 15
            reasons.append("Bullish MACD")

        else:

            score -= 15
            reasons.append("Bearish MACD")

        # =====================================
        # ADX
        # =====================================

        if technical["adx"] > 25:

            score += 10
            reasons.append("Strong Trend")

        # =====================================
        # Volume
        # =====================================

        if technical["volume_breakout"]:

            score += 10
            reasons.append("Volume Breakout")

        # =====================================
        # BOS
        # =====================================

        if smc["bos"] == "BULLISH BOS":

            score += 20
            reasons.append("Bullish BOS")

        elif smc["bos"] == "BEARISH BOS":

            score -= 20
            reasons.append("Bearish BOS")

        # =====================================
        # CHOCH
        # =====================================

        if smc["choch"] == "BULLISH CHOCH":

            score += 15
            reasons.append("Bullish CHOCH")

        elif smc["choch"] == "BEARISH CHOCH":

            score -= 15
            reasons.append("Bearish CHOCH")

        # =====================================
        # Order Blocks
        # =====================================

        if ob["bullish_order_block"]:

            score += 10
            reasons.append("Bullish Order Block")

        if ob["bearish_order_block"]:

            score -= 10
            reasons.append("Bearish Order Block")

        # =====================================
        # Fair Value Gap
        # =====================================

        if fvg["latest_bullish_fvg"]:

            score += 8
            reasons.append("Bullish FVG")

        if fvg["latest_bearish_fvg"]:

            score -= 8
            reasons.append("Bearish FVG")

        # =====================================
        # Support Resistance
        # =====================================

        if technical["price"] > sr["support"]:

            score += 5

        if technical["price"] < sr["resistance"]:

            score += 5

        # =====================================
        # Multi Timeframe
        # =====================================

        bullish = 0
        bearish = 0

        for timeframe, tf in mtf.items():

            # overall ko ignore karo
            if timeframe == "overall":
                continue

            trend = tf.get("trend")

            if trend == "BULLISH":

                bullish += 1

            elif trend == "BEARISH":

                bearish += 1

        if bullish > bearish:

            score += 15
            reasons.append("Multi TF Bullish")

        elif bearish > bullish:

            score -= 15
            reasons.append("Multi TF Bearish")

        # =====================================
        # Final Score
        # =====================================

        score = max(-100, min(score, 100))

        if score >= 60:

            signal = "STRONG BUY"

        elif score >= 25:

            signal = "BUY"

        elif score <= -60:

            signal = "STRONG SELL"

        elif score <= -25:

            signal = "SELL"

        else:

            signal = "WAIT"

        return {

            "score": score,

            "signal": signal,

            "reasons": reasons,

            "technical": technical,

            "smc": smc,

            "order_blocks": ob,

            "fvg": fvg,

            "support_resistance": sr,

            "multi_timeframe": mtf

        }