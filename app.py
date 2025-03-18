from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    # Add security headers
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Secure Python App!"})

@app.route('/api/data')
def get_data():
    user_input = request.args.get('query', '')
    # Sanitize user input to prevent injection attacks
    # This is a simple example - in production, use proper input validation
    sanitized_input = ''.join(c for c in user_input if c.isalnum() or c.isspace())
    return jsonify({"result": f"You queried: {sanitized_input}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)