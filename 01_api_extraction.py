import json
import os
from datetime import datetime, timezone

import requests


def fetch_google_shopping(query: str, api_key: str, gl: str = "us", hl: str = "en") -> dict:
	"""Call SerpAPI's Google Shopping endpoint and return the raw JSON response."""
	url = "https://serpapi.com/search"
	params = {
		"engine": "google_shopping",
		"q": query,
		"api_key": api_key,
		"gl": gl,
		"hl": hl,
	}

	response = requests.get(url, params=params, timeout=30)
	response.raise_for_status()
	return response.json()


def save_raw_json(data: dict, query: str, output_dir: str = "data/raw") -> str:
	"""Save the raw API response to a timestamped JSON file."""
	os.makedirs(output_dir, exist_ok=True)

	safe_query = query.replace(" ", "_").replace("/", "_")
	timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
	file_path = os.path.join(output_dir, f"google_shopping_{safe_query}_{timestamp}.json")

	with open(file_path, "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2, ensure_ascii=False)

	return file_path


def main() -> None:
	api_key = os.getenv("SERPAPI_API_KEY")
	if not api_key:
		raise RuntimeError("Set the SERPAPI_API_KEY environment variable first.")

	query = "electronics"
	data = fetch_google_shopping(query=query, api_key=api_key)

	print("Top-level keys:")
	print(list(data.keys()))

	shopping_results = data.get("shopping_results", [])
	print(f"\nFound {len(shopping_results)} shopping results")

	if shopping_results:
		first_item = shopping_results[0]
		print("\nFirst result keys:")
		print(list(first_item.keys()))

		print("\nFirst result preview:")
		print(json.dumps(first_item, indent=2, ensure_ascii=False)[:2000])

	saved_path = save_raw_json(data, query=query)
	print(f"\nSaved raw JSON to: {saved_path}")


if __name__ == "__main__":
	main()
