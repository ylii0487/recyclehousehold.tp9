from flask import Flask, render_template
import model

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():  # put application's code here
    return model.index_page()
    # return render_template('HomePage.html')

if __name__ == '__main__':
    app.run()
