from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hoje a Dama da SOFRENCIA MORREU"

if __name__ == '__main__':
    app.run()