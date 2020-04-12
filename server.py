from flask import Flask, render_template , request
from bson.json_util import dumps
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://solai_client:solairaj@cluster0-udyz3.mongodb.net/test?retryWrites=true&w=majority")
db = client.sample_mflix

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies', methods=['GET'])
def movies():
   collection = db.movies
   res = collection.find().limit(20)
   return dumps(res)

@app.route('/movies/language/<lang>', methods=['GET'])
def english_movies(lang):
   collection = db.movies
   res = collection.find({"languages":lang}).limit(20)
   return dumps(res)

@app.route('/movies/genere/<genere>', methods=['GET'])
def comedy_movies(genere):
   collection = db.movies
   res = collection.find({"genres":[genere]}).limit(20)
   if res == []:
      return 'No movies found'
   else:
      return dumps(res)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
