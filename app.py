from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://martinmaldonado:jwoaPcYmm1srsMil@cluster0.ul3g7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.Cluster0

@app.route('/')
def home():
    return "Hello, Flask with MongoDB! this is a test that this shit is working!"

if __name__ == "__main__":
    app.run(debug=True)
