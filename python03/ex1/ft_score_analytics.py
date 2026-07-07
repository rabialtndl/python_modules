import sys


def score_analytics() -> None:
    total_len = len(sys.argv)
    scores: list[int] = []

    for i in range(1, total_len):
        try:
            value = int(sys.argv[i])
            scores += [value]
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if not scores:
        print(
            "No scores provided. Usage: python3"
            f"{sys.argv[0]} <score1> <score2> ..."
            )
        return

    total_scores = sum(scores)
    number_of_players = len(scores)
    average_of_scores = total_scores / number_of_players
    score_range = max(scores) - min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {number_of_players}")
    print(f"Total score: {total_scores}")
    print(f"Average score: {average_of_scores}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
    print()
