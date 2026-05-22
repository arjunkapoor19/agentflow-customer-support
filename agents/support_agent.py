from tools.ticketing import ticketing_tool


class SupportAgent:
    def process_issue(self, issue_type):
        priority = "high" if issue_type == "refund" else "medium"

        ticket = ticketing_tool.create_ticket(
            issue_type=issue_type,
            priority=priority
        )

        return {
            "status": "processed",
            "ticket": ticket
        }