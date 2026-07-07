import random

ACHIEVEMENTS_POOL = [
    'Crafting Genius', 'World Savior', 'Master Explorer',
    'Collector Supreme', 'Untouchable', 'Boss Slayer',
    'Strategist', 'Speed Runner', 'Survivor',
    'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Unstoppable'
]


def gen_player_achievements() -> set[str]:
    count = random.randint(5, 9)
    random_selection = random.sample(ACHIEVEMENTS_POOL, count)
    return set(random_selection)


def main() -> None:
    a_ach = gen_player_achievements()
    b_ach = gen_player_achievements()
    c_ach = gen_player_achievements()
    d_ach = gen_player_achievements()
    print(f"Player Alice: {a_ach}")
    print(f"Player Bob: {b_ach}")
    print(f"Player Charlie: {c_ach}")
    print(f"Player Dylan: {d_ach}")
    all_dis = a_ach.union(b_ach, d_ach, c_ach)
    print()
    print(f"All distinct achievements: {all_dis}")
    common_achievements = a_ach.intersection(b_ach, d_ach, c_ach)
    print()
    print(f"Common achievements: {common_achievements}")
    print()
    print(f"Only Alice has: {a_ach.difference(b_ach, d_ach, c_ach)}")
    print(f"Only Bob has: {b_ach.difference(a_ach, d_ach, c_ach)}")
    print(f"Only Charlie has: {c_ach.difference(b_ach, d_ach, a_ach)}")
    print(f"Only Dylan has: {d_ach.difference(b_ach, a_ach, c_ach)}")
    print()
    print(f"Alice is missing: {all_dis.difference(a_ach)}")
    print(f"Bob is missing: {all_dis.difference(b_ach)}")
    print(f"Charlie is missing: {all_dis.difference(c_ach)}")
    print(f"Dylan is missing: {all_dis.difference(d_ach)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    main()
