from fastapi import APIRouter
import httpx

external_api=APIRouter()

@external_api.get("/api-consultation/{genre}", tags=['External Api'],)
async def api_consultation(genre:str):
    """
    Performs a query to an external API and returns the retrieved data.

    Args:
        genre (str): The genre used to filter the query.

    Returns:
        dict: The data retrieved from the external API in JSON format.
    """
    url = "https://randomuser.me/api/"

    params = {
        "genre": genre
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    return data
