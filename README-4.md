# Virtual Environmental Station using MQTT and ThingSpeak 🌍📡

This project simulates a virtual environmental IoT station that collects and sends sensor data to a cloud backend using MQTT and ThingSpeak.

## 💡 Overview

- Simulates three environmental sensors:
  - Temperature (-50°C to 50°C)
  - Humidity (0% to 100%)
  - CO₂ levels (300ppm to 2000ppm)
- Publishes sensor data to a public MQTT broker (`mqtt.eclipseprojects.io`)
- Subscribes to the topic and pushes the data to a ThingSpeak channel
- Visualizes the last 5 hours of sensor data using ThingSpeak's API and `matplotlib`

---

## 📂 Project Structure

| File | Description |
|------|-------------|
| `virtual_environmental_station.py` | Simulates virtual sensors and publishes data via MQTT |
| `thingspeak_publisher.py` | Subscribes to MQTT topic and pushes data to ThingSpeak |
| `display_last_5_hours_final_fix.py` | Fetches and plots last 5 hours of data for all sensors from ThingSpeak |

---

## 🛠️ How to Run

1. **Run the virtual station:**
   ```bash
   python3 virtual_environmental_station.py
   ```

2. **Run the ThingSpeak publisher:**
   ```bash
   python3 thingspeak_publisher.py
   ```

3. **Visualize last 5 hours of data:**
   ```bash
   python3 display_last_5_hours_final_fix.py
   ```

---

## 🔐 API Keys (Sample Configuration)

- **Write API Key** for ThingSpeak is used inside `thingspeak_publisher.py`
- **Read API Key** is used inside `display_last_5_hours_final_fix.py`
- Make sure to keep the keys updated in your script based on your private channel

---

## 📈 Sample Output

- Real-time terminal logs showing published and received sensor data
- ThingSpeak plots for:
  - Temperature (°C)
  - Humidity (%)
  - CO₂ (ppm)

---

## 🧠 Reflection

This project gave hands-on experience in building an end-to-end IoT pipeline using MQTT and ThingSpeak. It helped in understanding real-world data transmission, cloud integration, and debugging protocols for sensor networks.

---


