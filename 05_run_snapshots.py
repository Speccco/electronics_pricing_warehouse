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
    run_step("dbt snapshot", ["dbt", "snapshot"], DBT_PROJECT)


if __name__ == "__main__":
    main()
