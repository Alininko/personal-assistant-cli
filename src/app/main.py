from app.bootstrap import init_db
from app.interfaces.cli.app import app


def main() -> None:
    init_db()
    app()


if __name__ == "__main__":
    main()
