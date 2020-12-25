import click
from pizza import Pepperoni, Margherita, Hawaii, SizePizza
import processes_with_pizza
from processes_with_pizza import bake, pickup


@click.group()
def cli():
    pass


@cli.command()
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1)
@click.option("--delivery", default=False, is_flag=True)
def order(pizza: str, size: SizePizza, delivery: bool) -> None:
    """Готовит и доставляет пиццу."""
    pizza = pizza.lower().title()
    size = size.upper()
    pizza_class = globals()[pizza]  # получаем класс по его имени
    print(bake(pizza_class(size=size)))
    if delivery:
        print(processes_with_pizza.delivery(pizza_class(size=size)))
    else:
        print(pickup(pizza_class(size=size)))


@cli.command()
def menu() -> None:
    """Наше меню."""
    print(" " * 60, "😋 Наше меню 😋\n", end="")
    pizzas_list = [
        Pepperoni(size="L"),
        Pepperoni(size="XL"),
        Margherita(size="L"),
        Margherita(size="XL"),
        Hawaii(size="L"),
        Hawaii(size="XL"),
    ]
    for p in pizzas_list:
        print("-{pizza}".format(pizza=p))


if __name__ == "__main__":
    cli()
