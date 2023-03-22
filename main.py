from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route("/carousel")
def mercury():
    return f'''<!doctype html>
                    <html lang="en"
                    <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
                        <title>Пейзажи Марса</title>
                    </head>
                <body>
                    <h1>Пейзажи Марса</h1>
                <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <h1><img class="img-fluid d-inline w-75" src="{url_for('static', filename='img/mars1.png')}" 
                            alt="First slide"></h1>
                        </div>
                        <div class="carousel-item">
                            <h1><img class="img-fluid d-inline w-75" src="{url_for('static', filename='img/mars2.png')}" 
                            alt="Second slide"></h1>
                        </div>
                        <div class="carousel-item">
                            <h1><img class="img-fluid d-inline w-75" src="{url_for('static', filename='img/mars3.png')}" 
                            alt="Third slide"></h1>
                        </div>
                        <div class="carousel-item">
                            <h1><img class="img-fluid d-inline w-75" src="{url_for('static', filename='img/mars4.png')}" 
                            alt="Fourth slide"></h1>
                        </div>
                        <div class="carousel-item">
                            <h1><img class="img-fluid d-inline w-75" src="{url_for('static', filename='img/mars5.png')}" 
                            alt="Fifth slide"></h1>
                        </div>
                    </div>
                </div>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
