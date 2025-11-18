from .agent import agent


def main() -> None:
    query = "How secure an Agent, having authentication and authorization?"
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": query}
            ]
        }
    )
    # Print only the final assistant message
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
