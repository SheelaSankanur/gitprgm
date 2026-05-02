import streamlit as st
import requests
import os
import plotly.graph_objects as go
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables (API key)
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org"

def get_lat_lon(city):
    url = f"{BASE_URL}/geo/1.0/direct"
    params = {"q": city, "limit": 1, "appid": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code != 200 or len(response.json()) == 0:
        return None, None
    data = response.json()[0]
    return data["lat"], data["lon"]


def get_current_weather(lat, lon):
    url = f"{BASE_URL}/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None


def get_hourly_forecast(lat, lon):
    url = f"{BASE_URL}/data/2.5/forecast"
    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["list"][:24]  # next 24 hours
    return None


def get_daily_forecast(lat, lon):
    url = f"{BASE_URL}/data/2.5/forecast/daily"
    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric", "cnt": 5}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["list"][:5]  # 5 days
    return None


def plot_hourly_temp(temp_list, time_list):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=time_list,
            y=temp_list,
            mode="lines+markers",
            line={"color": "#007BFF", "width": 3},
            marker={"size": 6},
            name="Temperature",
        )
    )
    fig.update_layout(
        title="Hourly Temperature (Next 24 Hours)",
        xaxis_title="Time",
        yaxis_title="Temperature (°C)",
        template="plotly_white",
    )
    return fig


def plot_daily_temp(temp_list, day_list):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=day_list,
            y=temp_list,
            marker={"color": "#28A745"},
            text=temp_list,
            textposition="outside",
            name="Max/Min Temp",
        )
    )
    fig.update_layout(
        title="5‑Day Max Temperature",
        xaxis_title="Day",
        yaxis_title="Max Temperature (°C)",
        template="plotly_white",
    )
    return fig


def main():
    st.set_page_config(page_title="Weather Dashboard", layout="wide")
    st.title("🌤️ Global Weather Dashboard")

    # Sidebar: input and info
    with st.sidebar:
        st.header("📍 Search City")
        city = st.text_input("Enter city name (e.g., Bengaluru, London)", "")

        if city:
            lat, lon = get_lat_lon(city)
            if lat is None:
                st.error("City not found or invalid")
                st.stop()
            st.info(f"Lat: {lat:.4f}, Lon: {lon:.4f}")

    if not city:
        st.markdown("### Enter a city in the sidebar to start.")
        st.image(
            "https://images.unsplash.com/photo-1515776578871-53215666f5be",
            caption="Search any city worldwide",
            use_container_width=True,
        )
        st.stop()

    # Main: current weather
    st.header("Current Weather")
    current = get_current_weather(lat, lon)
    if current is None:
        st.error("Could not fetch current weather data. Check API key.")
        st.stop()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(
        "Temperature",
        f"{current['main']['temp']:.1f}°C",
        f"{current['main']['temp_min']:.1f}–{current['main']['temp_max']:.1f}°C",
    )
    col2.metric("Humidity", f"{current['main']['humidity']}%")
    col3.metric("Wind Speed", f"{current['wind']['speed']} m/s")
    col4.metric("Condition", current["weather"][0]["main"].title())

    # Hourly forecast chart
    st.header("Hourly Forecast (Next 24 Hours)")
    hourly = get_hourly_forecast(lat, lon)
    if hourly:
        times = [
            datetime.utcfromtimestamp(item["dt"]).strftime("%H:%M")
            for item in hourly
        ]
        temps = [item["main"]["temp"] for item in hourly]
        fig_hourly = plot_hourly_temp(temps, times)
        st.plotly_chart(fig_hourly, use_container_width=True)
    else:
        st.warning("Could not fetch hourly forecast.")

    # 5‑day forecast chart
    st.header("5‑Day Forecast")
    daily = get_daily_forecast(lat, lon)
    if daily:
        days = [datetime.utcfromtimestamp(d["dt"]).strftime("%a %d") for d in daily]
        max_temps = [d["temp"]["max"] for d in daily]
        fig_daily = plot_daily_temp(max_temps, days)
        st.plotly_chart(fig_daily, use_container_width=True)
    else:
        st.warning("Could not fetch 5‑day forecast.")

    # Footer
    st.markdown("---")
    st.markdown("Built with Python, Streamlit, and OpenWeatherMap API. 🌍")


if __name__ == "__main__":
    main()