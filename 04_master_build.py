from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
DBT_PROJECT = ROOT / "dbt_pricing" / "pricing_warehouse"


def run_step(step_name: str, command: list[str], cwd: Path) -> None:
	print(f"\n=== Running: {' '.join(command)} ===")
	subprocess.run(command, cwd=cwd, check=True)
	print(f"{step_name} step is done")


def main() -> None:
	run_step("API extraction", [sys.executable, str(ROOT / "01_api_extraction.py")], ROOT)
	run_step("Dataframe creation", [sys.executable, str(ROOT / "02_dataframe_creation.py")], ROOT)
	run_step("DuckDB load", [sys.executable, str(ROOT / "03_load_to_duckdb.py")], ROOT)
	run_step(
		"dbt build",
		["dbt", "build", "--exclude", "resource_type:snapshot"],
		DBT_PROJECT,
	)


if __name__ == "__main__":
	main()
