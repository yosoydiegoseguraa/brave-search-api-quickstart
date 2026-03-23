import requests

# This demo highlights Brave's Zero-Data-Retention (ZDR) infrastructure
# Optimized for high-throughput AI agent workflows.

def brave_search_demo(query):
    # Pro-tip: In a real environment, use an environment variable (os.getenv)
    api_key = "YOUR_BRAVE_API_KEY" 
    endpoint = f"https://api.search.brave.com/res/v1/web/search?q={query}"
    
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": api_key
    }

    print(f"📡 Querying Brave's independent index for: '{query}'...")
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Parsing for LLM Context Window efficiency
        results = data.get('web', {}).get('results', [])
        return results[:3] # Return top 3 for clean terminal output
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    # Example call that an AI Agent would perform
    results = brave_search_demo("Benefits of ZDR in LLM search indices")
    for r in results:
        print(f"Found: {r['title']} - {r['url']}")
