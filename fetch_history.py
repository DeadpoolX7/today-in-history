import requests
import datetime

# Get today's date
today = datetime.datetime.utcnow().strftime("%B_%d")  # Example: "February_25"

# Wikipedia API URL
URL = f"https://en.wikipedia.org/api/rest_v1/page/summary/{today}"

try:
    response = requests.get(URL)
    data = response.json()

    # Extract events from Wikipedia's summary
    events = data.get("extract", "No events found.").split("\n")

    # Format the output (top 3-5 events)
    formatted_events = "\n".join([f"- {event}" for event in events[:5]])

    # Update README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(f"# Today in History 📅\n\n📅 **{today.replace('_', ' ')}**\n\n")
        file.write(formatted_events + "\n")
        file.write("\n*(Auto-updated daily by GitHub Actions!)*\n")

    print("README.md updated successfully!")

except Exception as e:
    print("Error fetching data:", e)
