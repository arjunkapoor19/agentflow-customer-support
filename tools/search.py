class SearchTool:
    def search(self, query):
        return {
            "query": query,
            "results": [
                f"Result for '{query}'"
            ]
        }


search_tool = SearchTool()