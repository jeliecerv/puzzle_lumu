from urllib import request, error
import json


FRAGMENTS_SERVER = "http://localhost:8080/fragment?id={}"
final_fragment_text = {}


def get_fragment(fragment_id: int) -> list[dict]:
    """Fetch a fragment from the puzzle API."""

    url_fragment = FRAGMENTS_SERVER.format(fragment_id)
    try:
        with request.urlopen(url_fragment, timeout=1.0) as response:
            return json.loads(response.read().decode("utf-8"))
    except (error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        return []
    

def save_fragment_text(fragment: dict) -> None:
    """Save a fragment text to a file."""
    final_fragment_text[int(fragment["index"])] = fragment.get("text", "")


def main() -> None:
    """Main function to fetch and print fragments for a range of IDs."""
    for fragment_id in range(0, 100):  # Example range of fragment IDs
        fragment = get_fragment(fragment_id)
        if fragment:
            save_fragment_text(fragment)
        else:
            print(f"No fragment found for ID {fragment_id}.")

    final_fragment_sorted = dict(sorted(final_fragment_text.items()))
    print(" ".join(final_fragment_sorted.values()))  # Print the concatenated fragment texts

if __name__ == "__main__":
    main()