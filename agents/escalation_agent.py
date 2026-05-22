class EscalationAgent:
    def escalate(self, issue_summary):
        return {
            "escalated": True,
            "assigned_team": "human_support",
            "summary": issue_summary
        }