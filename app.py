from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)



@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        customernumber = details['cnum']
        firstName = details['fname']
        middleName = details['mname']
        lastName = details['lname']
        dateofBirth = details['dob']
        mobileno = details['mob']
        gender = details['gen']
        countryofbirth = details['cob']
        countryofresidence = details['cor']
        customerretailsegment  = details['crs']
        app.config['MYSQL_HOST'] = 'customer-details.c2gdkllibhae.us-east-1.rds.amazonaws.com'
        app.config['MYSQL_USER'] = 'admin'
        app.config['MYSQL_PASSWORD'] = 'Onmobile19'
        app.config['MYSQL_DB'] = 'Customer_Details'

        mysql = MySQL(app)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `Customer_New` (CustomerNumber, FirstName, MiddleName, LastName, DateOfBirth, MobileNumber, Gender, CountryOfBirth, CountryOfResidence, CustomerSegmentRetail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (customernumber, firstName, middleName, lastName, dateofBirth, mobileno, gender, countryofbirth, countryofresidence, customerretailsegment))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/')
def users():
	app.config['MYSQL_HOST'] = 'customer-details.c2gdkllibhae.us-east-1.rds.amazonaws.com'
	app.config['MYSQL_USER'] = 'admin'
	app.config['MYSQL_PASSWORD'] = 'Onmobile19'
	app.config['MYSQL_DB'] = 'Customer_Details'
	mysql = MySQL(app)
	cur = mysql.connection.cursor()
	cur.execute("SELECT * From Customer_New")
	data = cur.fetchall()
	cur.close()
	return  render_template('indexx.html', data=data)		 
if __name__ == '__main__':
    app.run('0.0.0.0')
