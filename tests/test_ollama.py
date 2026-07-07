from llm.factory import LLMFactory


def main():
    llm = LLMFactory.create()

    response = llm.generate(
        "Introduce yourself in one short sentence."
    )

    print("\nProvider :", response.provider)
    print("Model    :", response.model)
    print("Response :")
    print(response.text)


if __name__ == "__main__":
    main()