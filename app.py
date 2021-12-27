from argparse import ArgumentParser

from api.book.models import User

from api import app, login_manager


def setup_auth_service():
    pass


@login_manager.user_loader
def load_user(user):
    return User.query.get(user)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8888)
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)
