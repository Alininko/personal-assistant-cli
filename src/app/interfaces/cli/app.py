import typer

app = typer.Typer(
    name="assistant",
    help="Personal Assistant CLI — manage contacts, notes & birthdays.",
    no_args_is_help=True,
)

# TODO: register sub-commands:
# app.add_typer(contacts_app, name="contacts")
# app.add_typer(notes_app, name="notes")
