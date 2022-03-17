from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__, template_folder="template")
app.secret_key = "world"
app.permanent_session_lifetime = timedelta(days= 5)

@app.route("/login", methods= ["GET", "POST"])
def login():
    global logged_in
    if request.method == "POST":
        session.permanent = True
        name = request.form.get("name")
        session["user"] = name
        flash("Logged in!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        else:
            return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        name = session["user"]
        return render_template("user.html", user = name)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/")
def home():
    return render_template("index.html", context= "name")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if False:
    """elif logged_in[0] == True:
        return redirect(url_for("user", usr= logged_in[1]))"""
    #return redirect(url_for("user", usr= name))
    """@app.route("/<usr>")
    def user(usr):
        return f"Hello {usr}!"
    """

if __name__ == "__main__":
    app.run(debug= True)