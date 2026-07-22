"""
Prompt Builder
"""


class PromptBuilder:

    @classmethod
    def build(cls, context, user_message):

        analysis = context["analysis"]

        tech = analysis["technical"]

        return f"""
Live BTC Market

Price: {tech["price"]}

RSI: {tech["rsi"]}

EMA20: {tech["ema20"]}

EMA50: {tech["ema50"]}

Current Trading Signal

Signal:
{analysis["signal"]}

Direction:
{analysis["direction"]}

Confidence:
{analysis["confidence"]}%

Entry:
{analysis["entry"]}

Stop Loss:
{analysis["stop_loss"]}

TP1:
{analysis["tp1"]}

TP2:
{analysis["tp2"]}

TP3:
{analysis["tp3"]}

Reasons:

{chr(10).join("- "+r for r in analysis["reason"])}

===================================================

User Question:

{user_message}

===================================================

Instructions

If user greets you,
greet back naturally.

If user asks educational questions,
teach them.

If user asks about BTC,
answer using current market context.

If user asks about the signal,
explain WHY the current signal exists.

Do NOT calculate another signal.

Answer naturally like ChatGPT.

Avoid robotic wording.

Keep the response concise.
"""