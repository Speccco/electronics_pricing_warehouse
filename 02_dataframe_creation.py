from pathlib import Path
import json
from datetime import datetime, timezone

import pandas as pd

def main() -> None:
    raw_dir = Path("data/raw")
    raw_files = list(raw_dir.glob("google_shopping_*.json"))

    if not raw_files:
        raise FileNotFoundError("No raw shopping JSON files found in data/raw")

    latest_file = max(raw_files, key=lambda p: p.stat().st_mtime)

    with latest_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    captured_at = datetime.now(timezone.utc).isoformat()

    for item in data.get("shopping_results", []):
        rows.append({
            "query": data.get("search_parameters", {}).get("q"),
            "captured_at": captured_at,
            "product_id": item.get("product_id"),
            "position": item.get("position"),
            "title": item.get("title"),
            "product_link": item.get("product_link"),
            "source": item.get("source"),
            "source_icon": item.get("source_icon"),
            "multiple_sources": item.get("multiple_sources"),
            "price_text": item.get("price"),
            "full_price": item.get("extracted_old_price"),
            "price": item.get("extracted_price"),
            "tag": item.get("tag"),
            "second_hand_condition": item.get("second_hand_condition"),
            "rating": item.get("rating"),
            "reviews": item.get("reviews"),
            "delivery": item.get("delivery"),
            "extensions": item.get("extensions", [])
        })

    if not rows:
        print("No shopping results found.")
        return

    df = pd.DataFrame(rows)

    print(df.head())
    print(df.columns.tolist())
    print(df.shape)

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "shopping_results.parquet"
    df.to_parquet(output_path, index=False)
    print(f"Saved dataframe to {output_path}")


if __name__ == "__main__":
    main()