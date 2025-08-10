# app.py
import streamlit as st
import requests
import datetime
from coords import PROVINCE_COORDS, PROVINCE_CAPITALS
from weather_api import get_weather_forecast  # ← Chỉ import hàm mới

st.set_page_config(
    page_title="Thời tiết Việt Nam",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Ứng dụng Dự báo Thời tiết 63 tỉnh thành")
st.subheader("Chọn tỉnh và ngày để xem thông tin thời tiết (từ ngày mai đến 5 ngày tới).")

# Danh sách tỉnh
provinces = list(PROVINCE_COORDS.keys())
selected_province = st.selectbox("Chọn tỉnh/thành phố:", provinces, index=1)

# Chọn ngày dự báo 
today = datetime.date.today()
min_date = today + datetime.timedelta(days=1)
max_date = today + datetime.timedelta(days=5)  
selected_date = st.date_input("Chọn ngày dự báo:", min_value=min_date, max_value=max_date, value=min_date)

# Nút xem thời tiết (chỉ 1 lần)
if st.button("🌤️ Xem thời tiết"):
    with st.spinner(f"Đang lấy dữ liệu cho {selected_province} vào ngày {selected_date.strftime('%d/%m/%Y')}..."):
        weather = get_weather_forecast(selected_province, selected_date)
    
    if "error" in weather:
        st.error(f" Lỗi: {weather['error']}")
    else:
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
            st.subheader(f"{city} ({selected_date.strftime('%d/%m/%Y')})")
            st.markdown(f"**🌡️ Nhiệt độ:** {temp}°C (cảm giác như {feels_like}°C)")
            st.markdown(f"**💧 Độ ẩm:** {humidity}%")
            st.markdown(f"**🌬️ Gió:** {wind} m/s")

        st.success(f"📝 Mô tả: *{desc}*")

# Footer
st.markdown("---")
st.markdown("💬 Dự báo thời tiết từ OpenWeatherMap | App được phát triển bằng Python & Streamlit")