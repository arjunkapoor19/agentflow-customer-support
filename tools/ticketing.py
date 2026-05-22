class TicketingTool:
    def create_ticket(self, issue_type, priority):
        return {
            "ticket_id": "TICK-1024",
            "issue_type": issue_type,
            "priority": priority,
            "status": "created"
        }


ticketing_tool = TicketingTool()