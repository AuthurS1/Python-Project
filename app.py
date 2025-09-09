from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, static_folder="static")

# Load data từ file nếu có
todo = []
if os.path.exists("to.do"): # Kiểm tra nếu file "to.do" tồn tại
    with open("to.do", "r") as f:
        content = f.read().strip() # Đọc nội dung file, xóa khoảng trắng 2 đầu
        if content: # Nếu file không rỗng
            todo = eval(content) # Chuyển chuỗi thành list Python (nguy hiểm nếu có code độc hại)


@app.route("/") # Route trang chủ -> hiển thị danh sách todo
def index():
    return render_template("index.html", todo=todo) # Gửi danh sách todo sang file index.html để render

@app.route("/add", methods=["POST"]) # Route để thêm task mới (chỉ cho phép POST)
def add():
    name = request.form.get("name") 
    date = request.form.get("date")
    priority = request.form.get("priority")
    row = [name, date, priority]
    todo.append(row)

    # Lưu vào file
    with open("to.do", "w") as f:
        f.write(str(todo))

    return redirect("/") # Sau khi thêm xong thì quay lại trang chủ

@app.route("/remove/<name>") # Route để xóa task theo tên công việc
def remove(name):
    global todo
    todo = [row for row in todo if row[0] != name] # Giữ lại các task có tên khác với "name" (tức là xóa task trùng tên)

    # Lưu lại
    with open("to.do", "w") as f: # Lưu danh sách sau khi xóa vào fil
        f.write(str(todo))

    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) # Lấy PORT từ biến môi trường (dùng khi deploy Heroku/Render) Nếu không có thì mặc định là 5000
    app.run(host="0.0.0.0", port=port) # Chạy Flask app trên tất cả IP (0.0.0.0) để deploy online

