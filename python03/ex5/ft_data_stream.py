import random
from typing import Generator

PLAYERS = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS = ['run', 'eat', 'sleep', 'grab',
           'move', 'climb', 'swim', 'release', 'use']


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player_id = random.randint(0, len(PLAYERS) - 1)
        action_id = random.randint(0, len(ACTIONS) - 1)
        player = PLAYERS[player_id]
        action = ACTIONS[action_id]
        yield (player, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while (len(event_list) > 0):
        id = random.randint(0, len(event_list) - 1)
        chosen = event_list[id]
        event_list[:] = event_list[:id] + event_list[id + 1:]
        yield chosen


def main() -> None:
    events = gen_event()

    for i in range(1000):
        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = [next(events) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
