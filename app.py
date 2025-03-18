from flask import Flask, request, jsonify 
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    return jsonify({"message": "Welcome to the Secure Python App!"}) 
 
@app.route('/api/data') 
def get_data(): 
    user_input = request.args.get('query', '') 
    # Note: In a real app, sanitize user input to prevent injection attacks 
    return jsonify({"result": f"You queried: {user_input}"}) 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000) 
