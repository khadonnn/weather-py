# streamlit_app.py
import streamlit as st
import requests
from coords import PROVINCE_COORDS, PROVINCE_CAPITALS
from weather_api import get_current_weather  # Dùng lại hàm đã sửa

# Cấu hình trang
st.set_page_config(
    page_title="Dự báo thời tiết",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Ứng dụng Dự báo Thời tiết 63 tỉnh thành")
st.markdown("Chọn tỉnh để xem thông tin thời tiết chi tiết.")


# Danh sách tỉnh
provinces = list(PROVINCE_COORDS.keys())
selected_province = st.selectbox("Chọn tỉnh/thành phố:", provinces)

# Nút xem thời tiết
if st.button("🌤️ Xem thời tiết"):
    with st.spinner(f"Đang lấy dữ liệu cho {selected_province}..."):
        weather = get_current_weather(selected_province)
    
    if "error" in weather:
        st.error(f" Lỗi: {weather['error']}")
    else:
        # Hiển thị kết quả
        city = weather["city"]
        temp = weather["temp"]
        feels_like = weather["feels_like"]
        humidity = weather["humidity"]
        desc = weather["description"]
        wind = weather["wind_speed"]
        icon = weather["icon"]

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png", width=100)
        
        with col2:
            st.subheader(f"{city}")
            st.markdown(f"**🌡️ Nhiệt độ:** {temp}°C (cảm giác như {feels_like}°C)")
            st.markdown(f"**💧 Độ ẩm:** {humidity}%")
            st.markdown(f"**🌬️ Gió:** {wind} m/s")

        st.success(f"📝 Mô tả: *{desc}*")

# Footer
st.markdown("---")
st.markdown("💬 API từ OpenWeatherMap | App được phát triển bằng Python & Streamlit bởi chúng tôi")