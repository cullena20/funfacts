#!/usr/bin/env python3
import click
import db_facts
import os
import get_facts

# creates database if it doesn't exist
if not os.path.exists("facts.db"):
    get_facts.main()

conn = db_facts.connect()
cur = conn.cursor()


@click.command(help="See a fun fact!")
def main():
    click.echo(db_facts.display_fact(cur)[0][0])


if __name__ == "__main__":
    main()
