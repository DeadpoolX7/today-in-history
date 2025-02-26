import requests
import datetime
import sys

# Get today's date
today = datetime.datetime.now()
month = today.strftime("%-m")  # Get month as M (1-12)
day = today.strftime("%-d")    # Get day as D (1-31)
formatted_date = today.strftime("%B %d")  # For display (Example: "February 26")

# Muffinlabs History API URL
URL = f"https://history.muffinlabs.com/date/{month}/{day}"

try:
    # Make the request
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    # Extract events from the response (only from the 1990s)
    events = [
        f"{event['year']}: {event['text']}"
        for event in data.get("data", {}).get("Events", [])
        if 1990 <= int(event.get("year", 0)) <= 1999
    ]

    # Format the output
    formatted_events = "\n".join([f"- {event}" for event in events]) if events else "No events found from the 90s."

    # Update README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(f"# Today in History 📅\n\n")
        file.write(f"📅 **{formatted_date}**\n\n")
        file.write(formatted_events + "\n")
        file.write("\n*(Auto-updated daily by GitHub Actions!)*\n")

    print("README.md updated successfully!")

except requests.exceptions.RequestException as e:
    print(f"Network error occurred: {e}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error fetching data: {e}", file=sys.stderr)
    sys.exit(1)