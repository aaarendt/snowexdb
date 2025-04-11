import typer
from snowexdb.scripts.populate_database import db_populate_app

# The parent app that will contain all child apps for different script types
app = typer.Typer()

app.add_typer(db_populate_app, name="populate_database")

if __name__ == "__main__":
    app()
