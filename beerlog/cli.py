import typer
from core import add_beer_to_database

# black -l 79 <project_folder> - Formats the code to get rid of bad coding

main = typer.Typer(help="Beer Management Appication")


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
def list_beers(style: str):
    """Lists a beer"""
 
