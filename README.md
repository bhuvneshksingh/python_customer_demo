

# An example Django CRUD operation application

Install and run:

python -m venv env
pip install -r requirements.txt

Open `http://127.0.0.1:8000/` in your browser:

![Homepage](https://raw.githubusercontent.com/encode/starlette-example/master/docs/index.png)

Navigate to path that is not routed, eg `http://127.0.0.1:8000/nope`:

![Homepage](https://raw.githubusercontent.com/encode/starlette-example/master/docs/404.png)

Raise a server error by navigating to `http://127.0.0.1:8000/error`:

![Homepage](https://raw.githubusercontent.com/encode/starlette-example/master/docs/500.png)

Switch the `app = Starlette(debug=True)` line to `app = Starlette()` to see a regular 500 page instead.
