import requests
import datetime
import matplotlib.pyplot as plt

READ_API_KEY = "XHD340PCLOUPXFW6"
CHANNEL_ID = "2892593"
BASE_URL = "https://api.thingspeak.com/channels/{}/feeds.json"

def get_data(field, hours=5):
    end_time = datetime.datetime.now(datetime.timezone.utc)
    start_time = end_time - datetime.timedelta(hours=hours)
    url = BASE_URL.format(CHANNEL_ID)
    params = {
        "api_key": READ_API_KEY,
        "start": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end": end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    print(f"Requesting: {url} with params: {params}")
    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)
    print("Raw Text Sample:", response.text[:100])

    try:
        data = response.json()
        feeds = data.get("feeds", [])
        times = [entry["created_at"] for entry in feeds]
        values = [float(entry.get(f"field{field}", 0)) for entry in feeds]
        return times, values
    except Exception as e:
        print("Error:", e)
        return [], []

def plot_field(field, label):
    times, values = get_data(field)
    if times and values:
        plt.figure()
        plt.plot(times, values, marker='o')
        plt.xticks(rotation=45)
        plt.title(f"{label} - Last 5 Hours")
        plt.xlabel("Time")
        plt.ylabel(label)
        plt.tight_layout()
        plt.grid()
        plt.show()
    else:
        print(f"No data to plot for {label}")

plot_field(1, "Temperature (°C)")
plot_field(2, "Humidity (%)")
plot_field(3, "CO2 (ppm)")
