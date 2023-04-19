from flask import Flask, render_template, request

app = Flask(__name__)

# Create an empty list to store the questions and answers
qa_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the question and answer from the form submission
    question = request.form['question']
    answer = request.form['answer']

    # Add the question and answer to the list
    qa_list.append((question, answer))

    # Redirect back to the homepage
    return redirect('/')

@app.route('/view')
def view():
    # Render the questions and answers using an HTML template
    return render_template('view.html', qa_list=qa_list)
