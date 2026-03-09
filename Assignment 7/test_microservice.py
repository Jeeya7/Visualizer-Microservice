import requests
import json

# The URL where your app.py is running
url = "http://127.0.0.1:5000/visualize"

# Updated payload with dates that match the range
payload = {
    "spending_data": [
        {"cat": "Rent", "amt": 1200, "date": "2026-02-01"},
        {"cat": "Food", "amt": 400, "date": "2026-02-15"},
        {"cat": "Utilities", "amt": 150, "date": "2026-02-20"},
        {"cat": "Entertainment", "amt": 200, "date": "2026-02-25"}
    ],
    "date_range": {
        "start_date": "2020-02-01",
        "end_date": "2020-02-28"
    }
}

print("Sending Request to Visualizer Microservice")
try:
    response = requests.post(url, json=payload)
    result = response.json()
    
    if response.status_code == 200:
        print(result["chart"])
    else:
        print(f" Failed! Status Code: {response.status_code}")
        print("Error Message:", json.dumps(result, indent=4))

except Exception as e:
    print(f" An error occurred: {e}")