"""
Intent Detection Service
"""


class IntentService:

    GREETINGS = (
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "assalamualaikum",
        "assalamu alaikum",
        "salam",
        "yo",
    )

    THANKS = (
        "thanks",
        "thank you",
        "thx",
        "ty",
        "jazakallah",
        "jazak allah",
    )

    GOODBYE = (
        "bye",
        "goodbye",
        "see you",
        "see ya",
        "take care",
        "allah hafiz",
    )

    @classmethod
    def detect(cls, message: str) -> str:

        text = message.lower().strip()

        for word in cls.GREETINGS:
            if word in text:
                return "greeting"

        for word in cls.THANKS:
            if word in text:
                return "thanks"

        for word in cls.GOODBYE:
            if word in text:
                return "bye"

        return "ai"