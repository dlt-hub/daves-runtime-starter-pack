"""Downstream ping job -- fires whenever the fruitshop pipeline succeeds."""

from dlt.hub import run

from fruitshop_pipeline import load_shop


@run.job(
    trigger=load_shop.success,
    expose={"display_name": "Ping"},
)
def ping() -> None:
    print("ping")  # noqa: T201


if __name__ == "__main__":
    ping()
