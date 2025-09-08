from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, static_folder="static")

# Load data từ file nếu có
todo = []
if os.path.exists("to.do"):
    with open("to.do", "r") as f:
        content = f.read().strip()
        if content:
            todo = eval(content)

@app.route("/")
def index():
    return render_template("index.html", todo=todo)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    date = request.form.get("date")
    priority = request.form.get("priority")
    row = [name, date, priority]
    todo.append(row)

    # Lưu vào file
    with open("to.do", "w") as f:
        f.write(str(todo))

    return redirect("/")

@app.route("/remove/<name>")
def remove(name):
    global todo
    todo = [row for row in todo if row[0] != name]

    # Lưu lại
    with open("to.do", "w") as f:
        f.write(str(todo))

    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

