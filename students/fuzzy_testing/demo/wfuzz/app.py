from flask import Flask, request, render_template_string, make_response, redirect

app = Flask(__name__)

ROUTES = ["admin", "login", "dashboard", "api", "secret", "backup.bak"]

USERS = {"admin": "juandb", "bot": "pag*n*"}

SESSIONS = {}

LOGIN_TEMPLATE = """
<form method="POST">
  Usuario: <input name="username"><br>
  Contraseña: <input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
{% if error %}<p style='color:red'>{{ error }}</p>{% endif %}
"""


@app.route("/")
def index():
    return "<h1>Bienvenido a TADS</h1>"


@app.route("/FUZZ")
def fuzz_placeholder():
    return "Fuzz placeholder"


@app.route("/robots.txt")
def robots():
    return "Disallow: /admin\nDisallow: /secret"


@app.route("/<path:path>", methods=["GET", "POST"])
def catch_all(path):
    if path == "login":
        if request.method == "POST":
            u = request.form.get("username")
            p = request.form.get("password")
            if USERS.get(u) == p:
                resp = make_response(redirect("/dashboard"))
                resp.set_cookie("session", u)
                return resp
            return render_template_string(
                LOGIN_TEMPLATE, error="Credenciales inválidas"
            )
        return render_template_string(LOGIN_TEMPLATE)

    elif path == "dashboard":
        user = request.cookies.get("session")
        if user in USERS:
            return f"<h1>Hola, {user}</h1> Panel: config, users, /api/data"
        return redirect("/login")

    elif path == "admin":
        return "403 Prohibido", 403

    elif path == "secret":
        return "Nada que ver aquí", 404

    elif path == "api":
        param = request.args.get("debug")
        if param == "true":
            return "Debugging info: version 1.2.3"
        return "API endpoint: use ?debug=true"

    elif path == "backup.bak":
        return "# copia de seguridad del sistema..."

    return "Ruta no encontrada", 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
