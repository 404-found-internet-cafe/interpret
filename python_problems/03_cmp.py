
def compound(p, r, t, n=1):
    return round(p * ((1 + (r / n)) ** (t * n)), 2)










































def compound_interest(principal, rate, years, compounds_per_year=1):
    """
    Formula for getting the future value after compound interest.

    Source: https://w.wiki/G8ep#Periodic_compounding
    """
    growth_value = 1 + (rate / compounds_per_year)
    compounding_periods = compounds_per_year * years
    future_value = principal * (growth_value ** compounding_periods)
    future_value = round(future_value, 2)

    return future_value












































# Formula for getting the future value after compound interest
# https://w.wiki/G8ep#Periodic_compounding
compound = lambda p, r, t, n=1: round(p * ((1 + (r / n)) ** (t * n)), 2)









































































from rich.console import Console
from rich.text import Text

if __name__ == "__main__":
    console = Console()
    init_value = 100000
    interest_rate = 0.05
    time_in_years = 5

    text = Text.assemble(
        "\n",
        ("Initial value: ", "bold yellow"), f"AED {init_value:,.2f}\n",
        ("Interest rate: ", "bold yellow"), f"{interest_rate:.2%}\n",
        ("Time: ", "bold yellow"), f"{time_in_years} years\n",
        ("Compounds annually", "bold blue"), "\n"
    )
    future_value = compound(init_value, interest_rate, time_in_years)
    console.print(text)
    console.print(f"[bold yellow]Future value:[/bold yellow] AED {future_value:,.2f}")