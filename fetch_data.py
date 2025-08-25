import httpx

async def fetch_data(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        print(f"Error fetching data from {url}: {e}")
        return {"error": str(e)}