Description
The Visualizer microservice generates graphical representations (Pie Charts or Bar Graphs) of spending data. It helps users visually identify which categories consume the most budget.

Communication Contract
1. How to Programmatically REQUEST Data
To request a chart, send a POST request to the /visualize endpoint. The body of the request must be in JSON format.
Endpoint: http://localhost:5000/visualize
Method: POST
Request Parameters:
Parameter
Type
Description
type
String
The style of chart: "pie" or "bar".
data
Array
List of objects containing cat (Category Name), amt (Amount), and date (YYYY-MM-DD).
date_range
Object
Contains start_date and end_date (YYYY-MM-DD) to filter results.

Example Python Call:
Python
import requests

url = "http://localhost:5000/visualize"
payload = {
    "type": "pie",
    "data": [
        {"cat": "Rent", "amt": 1200, "date": "2024-01-01"},
        {"cat": "Food", "amt": 400, "date": "2024-01-05"}
    ],
    "date_range": {"start_date": "2024-01-01", "end_date": "2024-01-31"}
}
response = requests.post(url, json=payload)
print(response.json())


2. How to Programmatically RECEIVE Data
The microservice processes the data and returns a JSON response with a status and a link to the generated image.
Example Success Response:
JSON
{
  "status": "success",
  "chart_url": "http://localhost:5000/static/charts/chart_abc123.png"
}

Example Error Response:
(Occurs if the date range provided results in no data found)
JSON
{
  "status": "error",
  "message": "No data found for the given date range"
}
3. UML Sequence Diagram
This diagram shows the interaction between the Main Program and the Visualizer Microservice.
Code snippet
    sequenceDiagram
    participant Client as Main Program (Test Script)
    participant API as Visualizer Microservice
    
    Note over Client, API: Request Phase
    Client->>API: POST /visualize (JSON Payload)
    
    Note over API: Processing Phase
    API->>API: Filter data by date_range
    alt Data Exists
        API->>API: Generate Image (1080p optimized)
        API-->>Client: 200 OK (JSON with chart_url)
    else No Data Found
        API-->>Client: 400 Bad Request (JSON Error Message)
    end
    
    Note over Client: Client displays image from URL

Acceptance Criteria (Sprint 2 Plan)
Usability: Charts are generated in 10x6 inch format, optimized for 1080p readability.
Reliability: The service validates date ranges and prevents crashes if data is missing.
Performance: Average response time is under 500ms for standard datasets.
How to Run locally
Install dependencies: pip install flask matplotlib
Run the service: python app.py
Use the test_microservice.py script to verify the connection.

