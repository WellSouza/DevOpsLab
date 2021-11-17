from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hoje a Dama da SOFRENCIA MORREU - Mas hoje, ela vive em nossos corações!!"

if __name__ == '__main__':
    app.run()
