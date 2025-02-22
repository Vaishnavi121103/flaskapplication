from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
        name = "Vaishnavi Suryawanshi"  # Change this to your name
        username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
        server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')


        top_output = subprocess.getoutput("top -b -n 1")
        html = f"""
        <html>
        <body>
        <h2>Name: {name}</h2>
        <h3>Username: {username}</h3>
        <h3>Server Time: {server_time}</h3>
        <h3>TOP Output:</h3>
        <pre>{top_output}</pre>
        </body>
        </html>
        """

        return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    


