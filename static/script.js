// Hiện thông báo khi thêm task
document.addEventListener("DOMContentLoaded", () => { // Đợi cho đến khi toàn bộ nội dung HTML được load xong
    const form = document.querySelector(".todo-form"); // Lấy form thêm task (có class .todo-form)
    const message = document.createElement("div"); // Tạo một thẻ <div> để hiển thị thông báo
    message.className = "message"; // gán class cho div
    document.body.prepend(message); // đưa message lên đầu body

    form.addEventListener("submit", () => { // Khi submit form (thêm task mới)
        message.textContent = "✅ Task Added!"; // hiển thị nội dung thông báo
        message.style.display = "block"; // bật hiển thị
        setTimeout(() => { // sau 2 giây thì ẩn đi
            message.style.display = "none";
        }, 2000);
    });

    // Xác nhận trước khi xóa
    const deleteLinks = document.querySelectorAll(".delete"); // lấy tất cả nút xóa
    deleteLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            if (!confirm("Delete it?")) { // Nếu người dùng bấm "Cancel" thì chặn hành động xóa
                e.preventDefault();
            }
        });
    });

    // Lọc theo priority
    const filter = document.createElement("select");
    filter.innerHTML = `
        <option value="all">All</option>
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
    `;
    filter.className = "filter";
    document.querySelector(".container h1").after(filter);

    filter.addEventListener("change", () => {
        const value = filter.value;
        document.querySelectorAll(".todo-list li").forEach(li => {
            if (value === "all" || li.querySelector(".priority").classList.contains(value)) {
                li.style.display = "flex";
            } else {
                li.style.display = "none";
            }
        });
    });
});
