from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    name = "Steve"
    return render_template("bar_chart.html", name=name)

@app.route("/another")
def another_page():
    name = "Dave"
    return render_template("bar_chart2.html", name=name)

@app.route("/button-clicked", methods=["POST"])
def button_clicked():
    print("Button was clicked")
    name = "Rachael"
    return render_template("bar_chart.html", name=name)

# Start the Flask app
if __name__ == "__main__":
    app.run(port=5017)