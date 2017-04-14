from flask import Flask, render_template, app

app = Flask(__name__)

@app.route('/note')
def note_index():
    return render_template('notes.html')

if __name__ == '__main__':
    app.run(debug=True)
