from smolagents.tools import Tool


class TavilySearchTool(Tool):
    name = "tavily_search"
    description = """Performs a search using the Tavily Search API based on your query, 
    returning structured results."""
    inputs = {
        "query": {"type": "string", "description": "The search query to perform."}
    }
    output_type = "string"

    def __init__(self, api_key: str):
        super().__init__()
        try:
            from tavily import TavilyClient
        except ImportError as e:
            raise ImportError(
                "You must install package `tavily` to run this tool: for instance run `pip install tavily-python`."
            ) from e

        self.client = TavilyClient(api_key=api_key)

    def forward(self, query: str) -> str:
        try:
            # Perform a standard search
            results = self.client.search(query=query)["results"]
            if not results:
                raise Exception("No results found! Try a more general query.")

            # Format the results
            formatted_results = []
            for idx, result in enumerate(results):
                formatted_results.append(
                    f"{idx + 1}. [{result['title']}]({result['url']})\nScore: {result['score']}\nContent: {result['content']}"
                )

            return "## Search Results\n\n" + "\n\n".join(formatted_results)

        except Exception as e:
            return f"Error: {str(e)}"
