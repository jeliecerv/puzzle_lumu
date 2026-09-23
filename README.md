# puzzle_lumu

## How to run

Start the puzzle server:

```bash
docker run -p 8080:8080 ifajardov/puzzle-server
```

In another terminal, run the client from this directory:

```bash
python3 script.py
```

The script queries the API at `http://localhost:8080/fragment?id={id}` and prints the reconstructed message.

## Strategy

The first attempt used a brute-force approach by querying the API for a range of fragment IDs. It stored each fragment by its `index` and sorted the fragments before joining their text. This approach works, but sequential requests wait for each response before starting the next one.

The second attempt is faster because it uses `ThreadPoolExecutor` with 50 workers to make the API requests concurrently. This approach follows the message returned by the first run, which suggested making all requests at the same time.

## Steps completed

1. Queried a range of possible fragment IDs using a brute-force approach.
2. Stored each response by its fragment `index` instead of its query ID.
3. Sorted the fragments by index and joined their text to reconstruct the message.
4. Used the message from the first run as a clue to make requests concurrently.
5. Added a completion check that verifies the collected indexes are consecutive, starting at `0`.
6. Printed the reconstructed message only when the puzzle is complete.

## Performance

The number of workers was increased to meet the target execution time. The value of 50 workers was chosen at discretion as a practical configuration for this local test, rather than being required by the server. With this configuration, the puzzle completed successfully in approximately 0.84 seconds in a local run. The exact time may vary depending on server response times and the local environment.
