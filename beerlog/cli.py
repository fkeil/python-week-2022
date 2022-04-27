from typing import Optional

import typer  # documentacao da pra deixar colorido
from rich.console import Console
from rich.table import Table

from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="BMA - Beer Management Application")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(
        ...
    ),  # esse = typer.optional é o -- na hora de executar
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("\N{beer mug} beer added to database")
    else:
        print("no way")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """List beers in database"""
    beers = get_beers_from_database()
    table = Table(title="BeerLog :beer_mug: ")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
