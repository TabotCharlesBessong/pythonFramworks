from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def subjects():
  if request.method == 'POST':
    student = request.form.get('student')
    subjects = request.form.getlist('subjects')
    return render_template('subjects_result.html', student=student, subjects=subjects)
  return render_template('subjects_form.html')

if __name__ == '__main__':
  app.run(debug=True)