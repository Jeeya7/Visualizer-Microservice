Description
The Visualizer microservice provides graphical representations of spending data to help budget-conscious users identify which categories consume the most money. It processes a list of expenses and categories to return a chart.


Communication Contract
1. How to Programmatically REQUEST Data
To generate a chart, send a POST request to the /visualize endpoint. The request must include the following JSON parameters:

Parameter            Type            Description
spending_data        Array            Objects containing cat (category), amt (amount), and date (YYYY-MM-DD).

date_range           Object          Includes start_date and end_date to filter data.


Example Call (Python):
Python
import requests


url = "http://localhost:5000/visualize"
payload = {
    "spending_data": [
        {"cat": "Rent", "amt": 1200, "date": "2024-01-01"},
        {"cat": "Food", "amt": 400, "date": "2024-01-05"}
    ],
    "date_range": {"start_date": "2024-01-01", "end_date": "2024-01-31"}
}
response = requests.post(url, json=payload)


2. How to Programmatically RECEIVE Data
The microservice returns a JSON response containing the bar chart.
Success Response:
JSON
{
  "status": "success",
  "chart": "<strigified bar chart>"
}

3. UML Sequence Diagram
The following sequence diagram illustrates the programmatic request and receive flow.
Main Program (Test Script)       Visualizer API           ASCII Processing
          |                              |                           |
          |  POST /visualize             |                           |
          |  (JSON Data & Dates)         |                           |
          |----------------------------->|                           |
          |                              |                           |
          |                              | Filter Data by Date       |
          |                              |-------------------------->|
          |                              |                           |
          |                              | Scale & Render ASCII      |
          |                              |-------------------------->|
          |                              |                           |
          |                              |          Identify Max Val |
          |                              |          Calculate Ratios |
          |                              |          Build Star Bars  |
          |<-----------------------------|<--------------------------|
          |      Build JSON response     |      Return Text Chart    |
          |                              |                           |
          |<-----------------------------|                           |
          |  {"status":"success",        |                           |
          |   "chart":"..."}             |                           |
          |                              |                           |


Acceptance Criteria (Sprint 2 Plan)
Usability: Charts are clearly labeled and scaled for display.


Reliability: Returns an error message if the date range contains no data.


Performance: Returns the visualization within 500ms for datasets under 1000 entries.



How to Run Locally
Install Dependencies: pip install flask 
Start Service: python app.py
Run Test Script: python test_microservice.py


