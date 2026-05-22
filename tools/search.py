class SearchTool:
    def search(self, query, limit=5):
        return {
            "query": query,
            "results": [
                f"Result {i + 1} for '{query}'"
                for i in range(limit)
            ]
        }


search_tool = SearchTool()