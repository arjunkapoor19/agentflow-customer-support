from tools.search import search_tool
from tools.knowledge_base import knowledge_base_tool


class MemoryAgent:
    def retrieve_context(self, query):
        previous_context = search_tool.search(
            query=query,
            limit=2
        )

        kb_article = knowledge_base_tool.get_article(query)

        return {
            "memory_matches": previous_context,
            "knowledge_base": kb_article
        }