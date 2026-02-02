import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    # TRIGGER: This line reads directly from the URL parameters
    user_input = request.args.get("q")
    
    # TRIGGER: SQL Injection Vulnerability
    # Constructing a query by concatenating strings is a "Code Quality" and "Security" flaw.
    query = "SELECT * FROM items WHERE name = '" + user_input + "'"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # CodeQL will flag this line as a high-severity alert
    cursor.execute(query)
    
    results = cursor.fetchall()
    return str(results)

if __name__ == "__main__":
    app.run(debug=True)
  

## github="ghp_Rz8l2k3p5q0wMkkkkMM1m4n7v9x2zmmm8l2km3p5q0w1m4n"
###### aws="AKIAIMMMW6Q4XRANDOMKEY"
## stripe="sk_live_51Gqj58Lp9q2m4n6v8x0z1k3p5q7w9m2n4"
#hahahha
