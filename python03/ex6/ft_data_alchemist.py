import random


def data_alchemist() -> None:
    initial_list_of_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players : {initial_list_of_players}")
    capitalized_players = [name.capitalize()
                           for name in initial_list_of_players]
    print(f"New list with all names capitalized : {capitalized_players}")
    only_capitalized_players = [name for name in
                                initial_list_of_players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized_players}")
    print()
    score_dict = {name: random.randint(1, 1000)
                  for name in capitalized_players}
    print(f"Score dict: {score_dict}")
    score_dict_avg = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {score_dict_avg:.2f}")
    high_scores = {name: score for name, score
                   in score_dict.items() if score > score_dict_avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    data_alchemist()
