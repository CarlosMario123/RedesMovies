from flask import Flask,render_template #render template nos servira para renderizar el html
import data.dataMovies as data
import data.dataTrailer as dataTrailer
app = Flask(__name__)

@app.route('/')
def index():
    popular = data.getMoviesPopular()
    return render_template("index.html",populares=popular)

@app.route("/reproducir/<int:id>/<nombre>")
def reproducir(id, nombre):
    url = dataTrailer.obtenerUrlTrailer(id)
    print(url)
    return render_template("playFilm.html", id=id, nombre=nombre,urlFilm=url)

@app.route("/unservice")
def unservice():
    return render_template("noService.html")
if __name__ == '__main__':
    app.run(debug=True)