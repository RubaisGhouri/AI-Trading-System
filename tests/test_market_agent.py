from agents.market_agent import MarketAgent


def main():

    agent = MarketAgent()

    response = agent.analyze(
        symbol="BTCUSDT",
        timeframe="4H",
    )

    print()
    print("=" * 60)
    print("AGENT")
    print("=" * 60)
    print(agent.agent_name)

    print()
    print("=" * 60)
    print("RESPONSE")
    print("=" * 60)
    print(response.text)


if __name__ == "__main__":
    main()