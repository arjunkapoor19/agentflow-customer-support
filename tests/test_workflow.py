from agents.router_agent import RouterAgent
from agents.memory_agent import MemoryAgent


def test_router_agent():
    router = RouterAgent()

    response = router.route("refund for duplicate payment")

    assert response["assigned_agent"] == "support_agent"


def test_memory_agent():
    memory_agent = MemoryAgent()

    response = memory_agent.retrieve_context(
        "reset password"
    )

    assert "memory_matches" in response