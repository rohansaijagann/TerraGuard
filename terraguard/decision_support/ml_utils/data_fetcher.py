import requests
import datetime

def get_environmental_data(lat, lon):
    """
    Fetches live environmental data using free APIs.
    - Elevation & Current Weather: Open-Meteo Forecast
    - Annual Rainfall: Open-Meteo Archive (Last 365 days)
    - Soil pH, Nitrogen & SOC: ISRIC SoilGrids REST API
    """
    elevation = 600
    annual_rainfall = 1200
    soil_ph = 6.5
    nitrogen = 180
    soc = 45
    temp = 25.0
    humidity = 60
    wind_speed = 10.0
    is_water = False

    # 1. Fetch Elevation and Current Weather from Open-Meteo
    try:
        url_weather = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto"
        response = requests.get(url_weather, timeout=5)
        if response.status_code == 200:
            data = response.json()
            elevation = data.get('elevation', elevation)
            current = data.get('current', {})
            temp = current.get('temperature_2m', temp)
            humidity = current.get('relative_humidity_2m', humidity)
            wind_speed = current.get('wind_speed_10m', wind_speed)
            
            # If elevation is deep in the ocean (Arabian Sea)
            if elevation < -5:
                is_water = True
    except Exception as e:
        print(f"Weather API error: {e}")

    # 2. Fetch Annual Rainfall (Last 365 Days)
    monthly_rainfall = [0] * 12
    try:
        end_date = datetime.date.today() - datetime.timedelta(days=5)
        start_date = end_date - datetime.timedelta(days=365)
        url_rainfall = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date.isoformat()}&end_date={end_date.isoformat()}&daily=precipitation_sum"
        response = requests.get(url_rainfall, timeout=5)
        if response.status_code == 200:
            daily_precip = response.json().get('daily', {}).get('precipitation_sum', [])
            if daily_precip:
                clean_precip = [p if p is not None else 0 for p in daily_precip]
                annual_rainfall = sum(clean_precip)
                chunk_size = len(clean_precip) / 12.0
                for i in range(12):
                    start_idx = int(i * chunk_size)
                    end_idx = int((i + 1) * chunk_size)
                    monthly_rainfall[i] = round(sum(clean_precip[start_idx:end_idx]))
    except Exception as e:
        print(f"Rainfall API error: {e}")

    # 3. Fetch Soil pH, Nitrogen, and SOC (ISRIC SoilGrids)
    try:
        url_soil = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lat={lat}&lon={lon}&property=phh2o&property=nitrogen&property=soc&depth=0-5cm&value=mean"
        response = requests.get(url_soil, timeout=4)
        if response.status_code == 200:
            data = response.json()
            layers = data.get('properties', {}).get('layers', [])
            for layer in layers:
                prop_name = layer.get('name')
                depths = layer.get('depths', [])
                if depths:
                    mean_val = depths[0].get('values', {}).get('mean')
                    if mean_val is not None and mean_val > 0:
                        if prop_name == 'phh2o':
                            soil_ph = round(mean_val / 10.0, 1)
                        elif prop_name == 'nitrogen':
                            nitrogen = mean_val # cg/kg
                        elif prop_name == 'soc':
                            soc = mean_val # dg/kg
    except Exception as e:
        print(f"SoilGrids API error: {e}")

    return {
        "elevation": round(elevation),
        "annual_rainfall_mm": round(annual_rainfall),
        "monthly_rainfall": monthly_rainfall,
        "soil_ph": round(soil_ph, 1),
        "nitrogen": nitrogen,
        "soc": soc,
        "temp": round(temp, 1),
        "humidity": round(humidity),
        "wind_speed": round(wind_speed, 1),
        "is_water": is_water
    }

def get_live_forecast(lat, lon):
    """
    Fetches 7-day live weather forecast from Open-Meteo API.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode&timezone=auto"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Live forecast API error: {e}")
    return None