from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/identificacao")
def identificacao():
    return render_template("identificacao.html")

@app.route("/contexto")
def contexto():
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    return render_template("contexto.html", user_agent=user_agent, ip=ip)

if __name__ == "__main__":
    app.run()
