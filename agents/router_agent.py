from tools.search import search_tool


class RouterAgent:
    def route(self, user_query):
        search_results = search_tool.search(
            query=user_query,
            limit=3
        )

        if "refund" in user_query.lower():
            return {
                "assigned_agent": "support_agent",
                "reason": "Billing/refund intent detected",
                "search_results": search_results
            }

        return {
            "assigned_agent": "memory_agent",
            "reason": "General informational query",
            "search_results": search_results
        }