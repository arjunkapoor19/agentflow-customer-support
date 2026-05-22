class KnowledgeBaseTool:
    def get_article(self, topic):
        return {
            "topic": topic,
            "content": f"Knowledge base article for {topic}"
        }


knowledge_base_tool = KnowledgeBaseTool()