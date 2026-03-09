from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/visualize', methods=['POST'])
def visualize():
    content = request.json
    raw_data = content.get('spending_data', [])
    date_range = content.get('date_range', {})

    # 1. Filter data by date
    filtered_data = []
    # ... (Keep your existing date filtering logic here) ...
    if date_range.get('start_date') and date_range.get('end_date'):
        start = datetime.strptime(date_range['start_date'], '%Y-%m-%d')
        end = datetime.strptime(date_range['end_date'], '%Y-%m-%d')
        for entry in raw_data:
            entry_date = datetime.strptime(entry['date'], '%Y-%m-%d')
            if start <= entry_date <= end:
                filtered_data.append(entry)
    else:
        filtered_data = raw_data

    if not filtered_data:
        return jsonify({"status": "error", "message": "No data found"}), 400

    # 2. Scaling Logic
    MAX_BAR_WIDTH = 40  # The longest bar will be 40 stars
    
    # Find the maximum amount to use as a baseline
    max_amt = max(item['amt'] for item in filtered_data)
    
    chart_lines = ["--- Spending Visualization (Scaled) ---"]
    
    for item in filtered_data:
        cat = item['cat']
        amt = item['amt']
        
        # Calculate scaled stars: (Current / Max) * MaxWidth
        scaled_stars = int((amt / max_amt) * MAX_BAR_WIDTH)
        bar = "*" * scaled_stars
        
        # Format categories to align vertically
        chart_lines.append(f"{cat:<15} | {bar} (${amt})")

    chart = "\n".join(chart_lines)

    return jsonify({
        "status": "success",
        "chart": chart
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)