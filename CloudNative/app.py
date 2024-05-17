import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # Decorator specifying the route "/"
def index():
    cpuUsage = psutil.cpu_percent()
    memUsage = psutil.virtual_memory().percent

    msg = None
    if cpuUsage > 80 or memUsage > 80:
        msg = "High CPU or MEMORY utilisation detected. Please scale up"

    return render_template("index.html", cpu_metric=cpuUsage, mem_metric = memUsage, message = msg)
    # return f"CPU utilisation is : {cpuUsage} and MEMORY usage is : {memUsage}. {msg}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
