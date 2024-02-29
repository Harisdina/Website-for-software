from flask import Flask, render_template, url_for, request 
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Establish MySQL database connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='aprilfool',
            database='websoftware'
        )

        # Insert form data into MySQL Database
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customer (name, email, subject, message) VALUES (%s, %s, %s, %s)", (name, email, subject, message))
        connection.commit()
        
        connection.close()

        return 'Form submitted successfully'

@app.route('/submission', methods=['POST'])
def submission():
    if request.method == 'POST':
        messages = request.form['messages']

        # Establish MySQL database connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='aprilfool',
            database='websoftware'
        )

        # Insert feedback into MySQL Database
        cursor = connection.cursor()
        cursor.execute("INSERT INTO feedback (messages) VALUES (%s)", (messages,))
        connection.commit()
        
        connection.close()

        return 'Feedback submitted successfully'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
