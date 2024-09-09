# Importing required functions 
from flask import Flask, request, render_template 
import os

# Flask constructor 
app = Flask(__name__) 

# Root endpoint 
@app.route('/', methods=['GET']) 
def index(): 
	## Display the HTML form template 
	return render_template('my_home_page.html') 
    
#@app.route('/Yoruba_corpus') 
#def Yoruba_corpus(): 
	## Display the HTML form template 
	#return render_template('Yoruba_corpus.html') 
    

# `read-form` endpoint 
@app.route('/read-form', methods=['POST']) 
def read_form(): 

	# Get the form data as Python ImmutableDict datatype 
	data = request.form 

	## Return the extracted information 
	return {
        'userName': data['username'],
        'firstName': data['firstname'],
        'lastName': data['lastname'],
        'genderName': data['gendername'],
		'emailId'	 : data['emailAdd'], 
        'institutionName': data['institution'],
		'phoneNumber' : data['mobilenumber'], 
		'password' : data['userpassword'], 
	} 

# Root endpoint 
@app.route('/English_corpus', methods=['GET']) 
def English_corpus(): 
	## Display the HTML form template 
	return render_template('English_corpus.html') 


# `read-form` endpoint 
@app.route('/read-form', methods=['POST']) 
def read_form3(): 

	# Get the form data as Python ImmutableDict datatype 
	data3 = request.form 

	## Return the extracted information 
	return {
        'fileName': data2['filename'],
        'dataType': data2['datatype'],
        'accType': data2['accounttype'],
        'duration': data2['durations'],
	} 

# Root endpoint 
@app.route('/Yoruba_corpus', methods=['GET']) 
def Yoruba_corpus(): 
	## Display the HTML form template 
	return render_template('Yoruba_corpus.html') 

# `read-form` endpoint 
@app.route('/read-form', methods=['POST']) 
def read_form2(): 

	# Get the form data as Python ImmutableDict datatype 
	data2 = request.form 

	## Return the extracted information 
	return {
        'fileName': data2['filename'],
        'dataType': data2['datatype'],
        'accType': data2['accounttype'],
        'duration': data2['durations'],
	} 

# Root endpoint 
@app.route('/Transcript_page', methods=['GET']) 
def Transcript_page(): 
	## Display the HTML form template 
	return render_template('Transcript_page.html') 

# Root endpoint 
@app.route('/recorder') 
def recorder(): 
	## Display the HTML form template 
	return render_template('/js/recorder.js') 

# Root endpoint 
@app.route('/apps') 
def apps(): 
	## Display the HTML form template 
	return render_template('/js/apps.js') 

@app.route('/style') 
def style(): 
	## Display the HTML form template 
	return render_template('js/styel.css') 

#img = os.path.join("static", "Image")

#@app.route('/') 
#def home(): 
	## Display the HTML form template 
    #file = os.path.join(img, "pixe.jpg")
    #return render_template('home_page.html', image=file) 
    
@app.route('/Image/pixe') 
def pixe(): 
	## Display the HTML form template 
    return render_template('pixe.jpg') 

# Main Driver Function 
if __name__ == '__main__': 
	# Run the application on the local development server 
	app.run(debug=True)
