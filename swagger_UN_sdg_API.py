import requests

# Base URL mapping directly to the live UN SDG API endpoints defined in Swagger
BASE_URL = "https://un.org"

def get_sdg_goals():
    """
    Fetches the list of all Sustainable Development Goals (SDGs).
    Maps to the GET /v1/sdg/Goal/List Swagger endpoint.
    """
    url = f"{BASE_URL}/Goal/List"
    params = {"includechildren": "false"}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching goals: {e}")
        return None

def get_series_data(goal_code, geo_area_code=None):
    """
    Fetches actual temporal and indicator series data for a specific goal.
    Maps to the GET /v1/sdg/Goal/{goal}/Data Swagger endpoint.
    """
    url = f"{BASE_URL}/Goal/{goal_code}/Data"
    params = {}
    if geo_area_code:
        params["areaCode"] = geo_area_code  # Filter by specific M49 numeric country/region code
        
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for Goal {goal_code}: {e}")
        return None

if __name__ == "__main__":
    print("--- Fetching UN SDG Goals ---")
    goals = get_sdg_goals()
    if goals:
        for goal in goals[:3]:  # Displays a quick preview of the first few goals
            print(f"Goal {goal.get('code')}: {goal.get('title')}")
            
    print("\n--- Fetching Sample Data for Goal 1 (No Poverty) ---")
    sample_data = get_series_data(goal_code="1")
    if sample_data and len(sample_data) > 0:
        first_series = sample_data[0]
        print(f"Indicator: {first_series.get('indicator')}")
        print(f"Series Code: {first_series.get('seriesCode')}")
        print(f"Geographic Area: {first_series.get('geoAreaName')}")
        
        # Iterating through nested temporal points
        years_data = first_series.get('yearWiseData', [])
        for data_point in years_data[:5]:
            print(f"  Year {data_point.get('year')}: {data_point.get('value')}")