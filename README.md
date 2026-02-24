Description
The Visualizer microservice provides graphical representations of spending data to help budget-conscious users identify which categories consume the most money. It processes a list of expenses and categories to return a high-resolution chart.


Communication Contract
1. How to Programmatically REQUEST Data
To generate a chart, send a POST request to the /visualize endpoint. The request must include the following JSON parameters:

Parameter
Type
Description
spending_data
Array
Objects containing cat (category), amt (amount), and date (YYYY-MM-DD).
+1
chart_type
String
The desired chart style (e.g., "pie" or "bar").
+2
date_range
Object
Includes start_date and end_date to filter data.
+1

Example Call (Python):
Python
import requests


url = "http://localhost:5000/visualize"
payload = {
    "chart_type": "pie",
    "spending_data": [
        {"cat": "Rent", "amt": 1200, "date": "2024-01-01"},
        {"cat": "Food", "amt": 400, "date": "2024-01-05"}
    ],
    "date_range": {"start_date": "2024-01-01", "end_date": "2024-01-31"}
}
response = requests.post(url, json=payload)


2. How to Programmatically RECEIVE Data
The microservice returns a JSON response containing a public URL to the generated image.
Success Response:
JSON
{
  "status": "success",
  "chart_url": "http://localhost:5000/static/charts/chart_882.png"
}

Error Handling: If the provided date range contains no data, the service returns a JSON error message instead of a broken image to ensure system reliability.

3. UML Sequence Diagram
The following sequence diagram illustrates the programmatic request and receive flow.
Plaintext
Main Program (Test Script)       Visualizer API              Image Processing
          |                              |                           |
          |  POST /visualize             |                           |
          |  (JSON Data & Dates)         |                           |
          |----------------------------->|                           |
          |                              |                           |
          |                              | Filter Data by Date       |
          |                              |-------------------------->|
          |                              |                           |
          |                              | Generate Chart (1080p)    |
          |                              |-------------------------->|
          |                              |                           |
          |                              |             Analyze Data  |
          |                              |             Render Image  |
          |                              |             Save to File  |
          |                              |<--------------------------|
          |                              | Return Image URL          |
          |                              |                           |
          |      Build JSON response     |                           |
          |<-----------------------------|                           |
          |  {"status":"success",        |                           |
          |   "chart_url":"..."}         |                           |
          |                              |                           |


Acceptance Criteria (Sprint 2 Plan)
Usability: Charts are clearly labeled and optimized for 1080p monitors.


Reliability: Returns an error message if the date range contains no data.


Performance: Returns the visualization within 500ms for datasets under 1000 entries.



How to Run Locally
Install Dependencies: pip install flask matplotlib
Start Service: python app.py
Run Test Script: python test_microservice.py


