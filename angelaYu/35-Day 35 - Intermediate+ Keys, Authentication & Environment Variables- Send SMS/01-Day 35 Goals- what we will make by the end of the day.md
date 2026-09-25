Here is a structured breakdown of the Day 35 goals and the project you'll have built by the end of the day.

---

### 1. Skills Covered on Day 35

* **API authentication** — why valuable data requires identifying yourself
* **API keys** — getting and using one (OpenWeatherMap)
* **Twilio** — sending SMS (or WhatsApp) from Python
* **Environment variables** — keeping secrets out of your code
* Automation via PythonAnywhere or **GitHub Actions**

---

### 2. The Project: Rain Alert

Every morning the script:

1. Calls OpenWeatherMap with your API key.
2. Checks the next 12 hours of forecast for rain at your location.
3. If rain is coming → Twilio texts your phone: *"Bring an umbrella ☔"*.

---

### Summary Checklist

1. Keys authenticate; env variables hide them.
2. Two APIs chained: weather in, SMS out.
3. Scheduled in the cloud so it runs without you.
