# http://127.0.0.1:5000/?country=usa&source=facebook
# http://127.0.0.1:5000/s?k=laptop
# http://127.0.0.1:5000/portfolio/codebook
# http://127.0.0.1:5000/portfolio/json
# http://127.0.0.1:5000/portfolio/asd
# http://127.0.0.1:5000/about_us

from flask import Flask
from views import main

app=Flask(__name__)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)

