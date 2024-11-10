from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # for flashing messages

# MySQL Database Connection Configuration
db = mysql.connector.connect(
    host="localhost",      # Update with your MySQL host
    user="root",           # Update with your MySQL username
    password="password",   # Update with your MySQL password
    database="contactdb"   # Database created in Step 2
)

# Define routes for the application
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']
        
        # Insert data into MySQL database
        cursor = db.cursor()
        query = "INSERT INTO contacts (name, email, phone, subject, message) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, email, phone, subject, message))
        db.commit()
        cursor.close()
        
        flash("Thank you for reaching out! We'll get back to you soon.")
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)