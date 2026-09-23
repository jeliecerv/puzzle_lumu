# puzzle_lumu

The first attempt used a brute-force approach by querying the API for a range of fragment IDs. It works and reconstructs the final message by sorting the fragments by their index.

The second attempt is faster because it uses threads to make the API requests concurrently. This approach follows the message returned by the first run, which suggested making all requests at the same time.
