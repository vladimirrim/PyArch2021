FROM python:3.8

RUN python3.8 -m pip install Flask
RUN python3.8 -m pip install flask-login
RUN python3.8 -m pip install werkzeug
RUN python3.8 -m pip install ariadne
RUN python3.8 -m pip install argparse
RUN python3.8 -m pip install flask-sqlalchemy

WORKDIR /workspace

COPY . /workspace
RUN python3.8 /workspace/setup.py

ENTRYPOINT python3.8 /workspace/app.py --port 8888 --host ::