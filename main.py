from fastapi import FastAPI, Query
import httpx

app = FastAPI()

API_URL = "https://api.elhub.no/energy-data/v0/price-areas"

@app.get("/energy-data")
async def get_energy_data(
        start_date: str = Query(..., alias="startDate"),
        end_date: str = Query(..., alias="endDate")
):
    params = {
        "dataset": "CONSUMPTION_PER_GROUP_MBA_HOUR",
        "startDate": start_date,
        "endDate": end_date,
        "consumptionGroup": "household"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()