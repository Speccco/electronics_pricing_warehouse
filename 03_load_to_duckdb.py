from pathlib import Path

import duckdb


def main() -> None:
    db_path = Path("data/warehouse/pricing.duckdb")
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        try:
            with duckdb.connect(str(db_path)) as con:
                con.execute("SELECT 1")
        except duckdb.IOException:
            db_path.unlink()

    with duckdb.connect(str(db_path)) as con:
        con.execute("""
            CREATE SCHEMA IF NOT EXISTS raw;
        """)

        con.execute("""
            CREATE OR REPLACE TABLE raw.shopping_results AS
            SELECT *
            FROM read_parquet('data/processed/shopping_results.parquet')
        """)


if __name__ == "__main__":
    main()