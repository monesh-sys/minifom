from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)

# ---------- CSS ----------
animated_bg = """
<style>
body {
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial;
    color: white;
    background: linear-gradient(-45deg, #000000, #111111, #222222, #000000);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
}
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.container {
    background: rgba(0, 0, 0, 0.55);
    padding: 30px;
    width: 85%;
    max-width: 400px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(255,255,255,0.3);
    text-align: center;
}
h2 { font-size: 28px; margin-bottom: 20px; }
label { font-size: 18px; display:block; margin-top:10px; }
input[type="text"] {
    width: 100%;
    padding: 12px;
    margin: 5px 0;
    font-size: 16px;
    border: none;
    border-radius: 10px;
}
input[type="submit"] {
    width: 100%;
    padding: 14px;
    font-size: 18px;
    background: #00ffcc;
    border: none;
    border-radius: 10px;
    color: black;
    cursor: pointer;
    font-weight: bold;
}
.submitted-text { font-size: 18px; margin: 8px 0; }
</style>
"""

# ---------- HOME PAGE ----------
@app.route("/")
def home():
    return render_template_string(f"""
    <html>
    <head>{animated_bg}</head>
    <body>
        <div class="container">
            <h2>Mini Form</h2>
            <form action="/submit" method="POST">
                <label>Name</label>
                <input type="text" name="name" required>

                <label>Class</label>
                <input type="text" name="cls" required>

                <label>Section</label>
                <input type="text" name="sec" required>

                <input type="submit" value="Submit">
            </form>
        </div>
    </body>
    </html>
    """)

# ---------- SUBMIT ----------
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    cls = request.form.get("cls")
    sec = request.form.get("sec")

    # Save to CSV
    with open("form_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, cls, sec])

    # Print in terminal (you can see what user typed)
    print("NEW SUBMISSION:")
    print("Name:", name)
    print("Class:", cls)
    print("Section:", sec)
    print("---------------------")

    return render_template_string(f"""
    <html>
    <head>{animated_bg}</head>
    <body>
        <div class="container">
            <h2>Form Submitted</h2>
            <p class="submitted-text"><b>Name:</b> {name}</p>
            <p class="submitted-text"><b>Class:</b> {cls}</p>
            <p class="submitted-text"><b>Section:</b> {sec}</p>
        </div>
    </body>
    </html>
    """)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
