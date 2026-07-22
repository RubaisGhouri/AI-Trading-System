"""
QuantNova Chat Service
"""

class ChatService:

    @staticmethod
    def ask(message: str):

        message = message.lower()

        if "btc" in message:
            return (
                "BTC is currently the strongest monitored asset. "
                "Always confirm trend, RSI and volume before entering."
            )

        if "buy" in message:
            return (
                "Never buy only because of a signal. "
                "Always wait for confirmation from multiple indicators."
            )

        if "sell" in message:
            return (
                "Strong sell setups require bearish trend confirmation "
                "along with MACD and RSI alignment."
            )

        if "risk" in message:
            return (
                "Professional traders risk only 1-2% of capital per trade."
            )

        return (
            "QuantNova AI received your question. "
            "Advanced Gemini-powered responses will be connected next."
        )