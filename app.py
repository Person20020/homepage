from flask import Flask, render_template, request


app = Flask(__name__)

# Index
@app.route('/')
def index():
    return render_template('index.html')

# Projects
@app.route('/projects')
def projects():
    return render_template('projects.html')



# Hobbies
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/hobbies/coding')
def coding():
    return render_template('hobbies/coding.html')

@app.route('/hobbies/sailing')
def sailing():
    return render_template('hobbies/sailing.html')

@app.route('/hobbies/3dprinting')
def threedprinting():
    return render_template('hobbies/threedprinting.html')

@app.route('/hobbies/fpv')
def fpv():
    return render_template('hobbies/fpv.html')

@app.route('/hobbies/keyboards')
def keyboards():
    return render_template('hobbies/keyboards.html')


if __name__ == '__main__':
    app.run()