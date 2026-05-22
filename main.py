from agents.router_agent import RouterAgent
from agents.memory_agent import MemoryAgent
from agents.support_agent import SupportAgent


def run_demo():
    router = RouterAgent()
    memory_agent = MemoryAgent()
    support_agent = SupportAgent()

    route = router.route(
        "refund for accidental purchase"
    )

    context = memory_agent.retrieve_context(
        "refund policy"
    )

    support_response = support_agent.process_issue(
        "refund"
    )

    return {
        "route": route,
        "context": context,
        "support_response": support_response
    }


if __name__ == "__main__":
    result = run_demo()

    print(result)