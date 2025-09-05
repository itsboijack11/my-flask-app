from flask import Flask, render_template

# Initialize the Flask application with the name of the current module
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML template for the homepage

# About route
@app.route('/about')
def about():
    return render_template('about.html')  # Render the HTML template for the about page

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
