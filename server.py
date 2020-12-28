from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__) #__main__(file)


# @app.route('/')      #@ decorator
# def hello_world():
#     return 'Helloooooo!'
#
@app.route('/')
def template():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
#@app.route('/works.html')    #flask_templates
# def works():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')



#instead of above syntaxes copy and paste just simple do :
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline = '',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,  quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again'
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
# #             error = 'Invalid username/password'
# #     # the code below is executed if the request method
# #     # was GET or the credentials were invalid
# #     return render_template('login.html', error=error)
#
# @app.route('/submit_form', methods =['POST','GET'])
# def submit_form():
#     return 'Form has been Submitted'
