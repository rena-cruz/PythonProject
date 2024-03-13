from flask import Flask, render_template

app = Flask(__name__)

# route ->
# função -> o que será exibindo na página
# template

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/contatos')
def contatos():
    return render_template("contatos.html")

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
