import requests
import json

# The URL where your microservice is running
URL = "http://localhost:5000/visualize"  # Adjust port as needed

# 1. Prepare the data based on your communication contract
payload = {
    "type": "pie",
    "data": [
        {"cat": "Rent", "amt": 1200, "date": "2024-01-01"},
        {"cat": "Food", "amt": 400, "date": "2024-01-05"},
        {"cat": "Entertainment", "amt": 150, "date": "2024-01-10"}
    ],
    "date_range": {
        "start_date": "2024-01-01", 
        "end_date": "2024-01-31"
    }
}

# 2. Programmatically REQUEST data from the microservice
print("Sending request to Visualizer Microservice...")
try:
    response = requests.post(URL, json=payload)
    
    # 3. Programmatically RECEIVE data from the microservice
    if response.status_code == 200:
        result = response.json()
        print("Success!")
        print(f"Status: {result.get('status')}")
        print(f"Chart URL: {result.get('chart_url')}")
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Failed to connect to the microservice: {e}")