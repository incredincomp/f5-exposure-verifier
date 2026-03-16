"""CLI entrypoint using Typer."""

import typer

app = typer.Typer(
    name="f5-verifier",
    help="F5 Exposure Verifier CLI",
    no_args_is_help=True,
)


@app.command()
def serve(
    host: str = typer.Option("0.0.0.0", help="Bind host"),
    port: int = typer.Option(8000, help="Bind port"),
    reload: bool = typer.Option(False, help="Enable auto-reload"),
) -> None:
    """Start the API server."""
    import uvicorn

    uvicorn.run("app.main:app", host=host, port=port, reload=reload)


@app.command()
def db_upgrade() -> None:
    """Run Alembic database migrations."""
    from alembic import command
    from alembic.config import Config

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    app()
