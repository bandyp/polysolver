from flask import Flask, render_template
from poly import x, y, coeff, mymodel, rootsp, myline, fig

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def polynomial_solver():
    return render_template('home.html', x=x, y=y, coeff=coeff, mymodel=mymodel, rootsp=rootsp, myline=myline, fig=fig)


if __name__ == "__main__":
    app.run(debug=True)