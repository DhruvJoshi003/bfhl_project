# backend/app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({
            "operation_code": 1
        })

    if request.method == 'POST':
        data = request.json.get('data', [])
        user_id = "john_doe_17091999"  # Replace with your format
        email = "john@xyz.com"  # Replace with your email
        roll_number = "ABCD123"  # Replace with your roll number

        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        lowercase_alphabets = [x for x in alphabets if x.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
