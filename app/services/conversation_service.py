"""
Conversation Responses
"""


class ConversationService:

    @staticmethod
    def greeting():

        return (
            "👋 Hello! Welcome to QuantNova AI.\n\n"
            "I'm your AI Trading Assistant developed by Rubais Ghouri "
            "and powered by DevSpark Creations.\n\n"
            "I can help you with:\n"
            "• Live BTC Market Analysis\n"
            "• Crypto Trading Strategies\n"
            "• Technical Analysis\n"
            "• Smart Money Concepts\n"
            "• Risk Management\n\n"
            "How can I help you today?"
        )

    @staticmethod
    def thanks():

        return (
            "You're welcome! 😊 "
            "If you need market analysis, trading guidance, or help understanding any trading concept, I'm always here to assist."
        )

    @staticmethod
    def goodbye():

        return (
            "👋 Goodbye! Trade safely, manage your risk wisely, and have a great day. I'll be here whenever you need assistance."
        )