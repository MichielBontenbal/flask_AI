 from flask import Flask, request, jsonify, render_template
 

 app = Flask(__name__)
 

 @app.route('/')
 def index():
  return render_template('index.html') # Make sure 'index.html' is in a 'templates' folder
 

 @app.route('/process_text', methods=['POST'])
 def process_text():
  data = request.get_json()
  text = data['text']
  
  # Process the text (e.g., store it, analyze it, etc.)
  processed_text = text.upper() # Example: Convert to uppercase
 

  return jsonify({'message': 'Text received and processed!', 'processed_text': processed_text})
 

 if __name__ == '__main__':
  app.run(debug=True)