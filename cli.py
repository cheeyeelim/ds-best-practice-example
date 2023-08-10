"""Console script for ds-best-practice-example."""
import click

from ezml.pipeline import linear_regression_pipeline


@click.command()
def main() -> None:
    """Main entrypoint for command line."""
    click.echo("ds-best-practice-example")
    click.echo("=" * len("ds-best-practice-example"))
    click.echo("Showcase best practices for structuring a DS-related Python package/application.")
    click.echo("This example package will fit a linear regression on your input data.")
    click.echo("It comes with the `diabetes` data as a toy data.")

    # Execute pipeline
    linear_regression_pipeline()


if __name__ == "__main__":
    main()  # pragma: no cover
