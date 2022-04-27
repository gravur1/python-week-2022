import typer
from typing import Optional
from core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console

# black -l 79 <project_folder> - Formats the code to get rid of bad coding

main = typer.Typer(help="Beer Management Appication")

console = Console()


@main.command("add")
# python beerlog add --help
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer into the db"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to database")
    else:
        print("Failed to add beer to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists a beer"""
    beers = get_beers_from_database()
    table = Table(title="Beerlog 🍺 ")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [
            str(getattr(beer, header)) for header in headers
        ]  # beer.name, beer.id
        table.add_row(*values)
    console.print(table)
