# weather_api.py
import requests
from config import API_KEY, FORECAST_URL, UNITS, LANGUAGE
from coords import PROVINCE_COORDS, PROVINCE_CAPITALS
from datetime import datetime

def get_weather_forecast(province_name, target_date):
    """
    Lấy dự báo thời tiết cho tỉnh vào ngày cụ thể (dùng OpenWeather Forecast API)
    """
    if province_name not in PROVINCE_COORDS:
        return {"error": f"Không tìm thấy tọa độ cho: {province_name}"}

    lat, lon = PROVINCE_COORDS[province_name]
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': UNITS,
        'lang': LANGUAGE
    }

    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        if response.status_code != 200:
            return {"error": f"API lỗi {response.status_code}: {response.json().get('message', '')}"}

        data = response.json()
        forecasts = data['list']

        # Tìm bản ghi gần giữa ngày (khoảng 12h)
        target_str = target_date.strftime('%Y-%m-%d')
        candidates = []

        for item in forecasts:
            dt = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
            if dt.strftime('%Y-%m-%d') == target_str:
                candidates.append(item)

        if not candidates:
            return {"error": f"Không có dữ liệu cho ngày {target_str}. Chỉ có dữ liệu trong 5 ngày tới."}

        # Chọn bản ghi gần 12h nhất
        best = min(candidates, key=lambda x: abs(x['dt_txt'].count('12:') and 0 or 12))

        # Lấy giờ để chọn gần trưa
        best = min(candidates, key=lambda x: abs(datetime.strptime(x['dt_txt'], '%Y-%m-%d %H:%M:%S').hour - 12))

        city_name = data['city']['name']

        return {
            "city": PROVINCE_CAPITALS.get(province_name, province_name),
            "province": province_name,
            "temp": round(best['main']['temp'], 1),
            "feels_like": round(best['main']['feels_like'], 1),
            "humidity": best['main']['humidity'],
            "description": best['weather'][0]['description'].capitalize(),
            "wind_speed": best.get('wind', {}).get('speed', "N/A"),
            "icon": best['weather'][0]['icon'],
        }

    except Exception as e:
        return {"error": f"Lỗi kết nối: {str(e)}"}