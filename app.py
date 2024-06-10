from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_data():
    conn = psycopg2.connect(
        dbname=os.environ["POSTGRESQL_DB"], 
        user=os.environ["POSTGRESQL_USER"], 
        password=os.environ["POSTGRESQL_PASSWORD"], 
        host=os.environ["POSTGRESQL_HOST"], 
        port=os.environ["POSTGRESQL_PORT"],
        sslmode='require'
    )
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {os.environ["POSTGRESQL_TABLE"]} LIMIT 1')
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

@app.route('/')
def index():
    data = get_db_data()
    return f'<h1>This is a Test Message.</h1>\n<h3>The Example Query should be below:</h3>\n<p>{data}</p>'
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
