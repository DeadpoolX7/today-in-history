import requests
import datetime

# Get today's date
today = datetime.datetime.now()
month = today.strftime("%m")  # Get month as MM
day = today.strftime("%d")    # Get day as DD
formatted_date = today.strftime("%B %d")  # For display (Example: "February 26")

# Wikipedia API URL for "On This Day" events
BASE_URL = "https://api.wikipedia.org/feed/v1/wikipedia/en/onthisday/selected"
URL = f"{BASE_URL}/{month}/{day}"

try:
    # Add proper headers as required by Wikipedia API
    headers = {
        "User-Agent": "TodayInHistory/1.0 (https://github.com/DeadpoolX7/today-in-history)"
    }
    
    response = requests.get(URL, headers=headers, timeout=30)
    response.raise_for_status()  # Raise exception for bad status codes
    data = response.json()

    # Extract events from the response
    # The API returns events in a different structure
    events = []
    if "selected" in data:
        for event in data["selected"][:5]:  # Get top 5 events
            year = event.get("year", "")
            text = event.get("text", "")
            events.append(f"{year}: {text}")

    # Format the output
    formatted_events = "\n".join([f"- {event}" for event in events]) if events else "No events found."

    # Update README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(f"# Today in History 📅\n\n")
        file.write(f"📅 **{formatted_date}**\n\n")
        file.write(formatted_events + "\n")
        file.write("\n*(Auto-updated daily by GitHub Actions!)*\n")

    print("README.md updated successfully!")

except Exception as e:
    print("Error fetching data:", e)
