# weather_api.py
import requests
from config import API_KEY, BASE_URL, UNITS, LANGUAGE
from coords import PROVINCE_COORDS

PROVINCE_CAPITALS = {
    "Hà Nội": "Hà Nội",
    "Hồ Chí Minh": "TP. Hồ Chí Minh",
    "Đà Nẵng": "Đà Nẵng",
    "Hải Phòng": "Hải Phòng",
    "Cần Thơ": "Cần Thơ",
    "An Giang": "Long Xuyên",
    "Bà Rịa - Vũng Tàu": "Vũng Tàu",
    "Bắc Giang": "Bắc Giang",
    "Bắc Kạn": "Bắc Kạn",
    "Bạc Liêu": "Bạc Liêu",
    "Bắc Ninh": "Bắc Ninh",
    "Bến Tre": "Bến Tre",
    "Bình Định": "Quy Nhơn",
    "Bình Dương": "Thủ Dầu Một",
    "Bình Phước": "Đồng Xoài",
    "Bình Thuận": "Phan Thiết",
    "Cà Mau": "Cà Mau",
    "Cao Bằng": "Cao Bằng",
    "Đắk Lắk": "Buôn Ma Thuột",
    "Đắk Nông": "Gia Nghĩa",
    "Điện Biên": "Điện Biên Phủ",
    "Đồng Nai": "Biên Hòa",
    "Đồng Tháp": "Cao Lãnh",
    "Gia Lai": "Pleiku",
    "Hà Giang": "Hà Giang",
    "Hà Nam": "Phủ Lý",
    "Hà Tĩnh": "Hà Tĩnh",
    "Hải Dương": "Hải Dương",
    "Hậu Giang": "Vị Thanh",
    "Hòa Bình": "Hòa Bình",
    "Hưng Yên": "Hưng Yên",
    "Khánh Hòa": "Nha Trang",
    "Kiên Giang": "Rạch Giá",
    "Kon Tum": "Kon Tum",
    "Lai Châu": "Lai Châu",
    "Lâm Đồng": "Đà Lạt",
    "Lạng Sơn": "Lạng Sơn",
    "Lào Cai": "Lào Cai",
    "Long An": "Tân An",
    "Nam Định": "Nam Định",
    "Nghệ An": "Vinh",
    "Ninh Bình": "Ninh Bình",
    "Ninh Thuận": "Phan Rang",
    "Phú Thọ": "Việt Trì",
    "Phú Yên": "Tuy Hòa",
    "Quảng Bình": "Đồng Hới",
    "Quảng Nam": "Tam Kỳ",
    "Quảng Ngãi": "Quảng Ngãi",
    "Quảng Ninh": "Hạ Long",
    "Quảng Trị": "Đông Hà",
    "Sóc Trăng": "Sóc Trăng",
    "Sơn La": "Sơn La",
    "Tây Ninh": "Tây Ninh",
    "Thái Bình": "Thái Bình",
    "Thái Nguyên": "Thái Nguyên",
    "Thanh Hóa": "Thanh Hóa",
    "Thừa Thiên Huế": "Huế",
    "Tiền Giang": "Mỹ Tho",
    "Trà Vinh": "Trà Vinh",
    "Tuyên Quang": "Tuyên Quang",
    "Vĩnh Long": "Vĩnh Long",
    "Vĩnh Phúc": "Vĩnh Yên",
    "Yên Bái": "Yên Bái",
}


def get_current_weather(province_name):
    if province_name not in PROVINCE_COORDS:
        return {"error": f"Không tìm thấy tọa độ cho: {province_name}"}

    lat, lon = PROVINCE_COORDS[province_name]
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": UNITS,
        "lang": LANGUAGE,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": PROVINCE_CAPITALS.get(province_name, province_name),
                "province": province_name,
                "temp": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].capitalize(),
                "wind_speed": data.get("wind", {}).get("speed", "N/A"),
                "icon": data["weather"][0]["icon"],
            }
        else:
            return {
                "error": f"API lỗi {response.status_code}: {response.json().get('message', '')}"
            }
    except Exception as e:
        return {"error": f"Kết nối thất bại: {str(e)}"}
