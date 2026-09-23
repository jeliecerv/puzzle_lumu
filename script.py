from urllib import request, error
import json
from concurrent.futures import ThreadPoolExecutor


FRAGMENTS_SERVER = "http://localhost:8080/fragment?id={}"
MAX_FRAGMENTS = 80
MAX_WORKERS = 50
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

def fetch_and_save(fragment_id: int) -> None:
    fragment = get_fragment(fragment_id)
    if fragment:
        save_fragment_text(fragment)

def call_all_request_same_time() -> None:
    """Call all requests at the same time using threads."""
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(fetch_and_save, range(0, MAX_FRAGMENTS))

def is_completed() -> bool:
    """Check if all fragments have been fetched."""
    if not final_fragment_text:
        return False

    indexes = sorted(final_fragment_text)
    return indexes == list(range(indexes[-1] + 1))

def main() -> None:
    """Main function to fetch and print fragments for a range of IDs."""
    call_all_request_same_time()

    if is_completed():
        final_fragment_sorted = dict(sorted(final_fragment_text.items()))
        print(" ".join(final_fragment_sorted.values()))
    else:
        print("The puzzle is incomplete.")

if __name__ == "__main__":
    main()