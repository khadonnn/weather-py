# main.py
from utils import load_provinces, find_province
from weather_api import get_current_weather
import os

def main():
    print("🌤️ Ứng dụng Dự báo Thời tiết 63 tỉnh thành Việt Nam")
    print("Gõ 'thoat', 'exit' hoặc 'quit' để dừng.\n")
    
    # Tải danh sách tỉnh
    provinces = load_provinces()
    
    while True:
        user_input = input("📍 Nhập tên tỉnh: ").strip()
        if user_input.lower() in ['thoat', 'exit', 'quit']:
            print("👋 Cảm ơn bạn đã sử dụng!")
            break
        
        # Tìm tỉnh phù hợp
        matches = find_province(user_input, provinces)
        if not matches:
            print(" Không tìm thấy tỉnh nào phù hợp. Vui lòng thử lại.\n")
            continue
        
        # Chọn tỉnh đầu tiên
        province = matches[0]
        print(f"🔍 Đang lấy dữ liệu cho: {province}...\n")
        
        weather = get_current_weather(province)
        
        if "error" in weather:
            print(f" Lỗi: {weather['error']}\n")
        else:
            print(f"🏛️  Thành phố: {weather['city']}")
            print(f"🌡️  Nhiệt độ: {weather['temp']}°C (cảm giác như {weather['feels_like']}°C)")
            print(f"💧 Độ ẩm: {weather['humidity']}%")
            print(f"📝 Mô tả: {weather['description']}")
            print(f"🌬️  Tốc độ gió: {weather['wind_speed']} m/s")
            print(f"🖼️  Icon: http://openweathermap.org/img/wn/{weather['icon']}@2x.png")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()