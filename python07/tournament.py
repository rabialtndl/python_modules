from typing import List, Tuple
from ex0.Creature_Factory import AquaFactory, CreatureFactory, FlameFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    StrategyError,
)


def tournament_begin(
        opponents: List[Tuple[CreatureFactory, BattleStrategy]],
        title: str,
        description: str
) -> None:
    print(f"\nTournament {title}")
    print(description)
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            fighter1 = factory1.create_base()
            fighter2 = factory2.create_base()

            print(fighter1.describe())
            print(" vs.")
            print(fighter2.describe())
            print(" now fight!")

            try:
                strategy1.act(fighter1)
                strategy2.act(fighter2)
            except StrategyError as ex:
                print(f"Battle error, aborting tournament: {ex}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transforming_factory = TransformCreatureFactory()

    normal_s = NormalStrategy()
    aggressive_s = AggressiveStrategy()
    defensive_s = DefensiveStrategy()

    tournmanet_zero = [
        (flame_factory, normal_s),
        (healing_factory, defensive_s)
        ]

    tournament_begin(tournmanet_zero, "0 (basic)",
                     "[ (Flameling+Normal), (Healing+Defensive) ]")
    tournament_first = [
        (flame_factory, aggressive_s),
        (healing_factory, defensive_s)
        ]

    tournament_begin(tournament_first, "1 (error)",
                     "[ (Flameling+Aggressive), (Healing+Defensive) ]")

    tournament_second = [
        (aqua_factory, normal_s),
        (healing_factory, defensive_s),
        (transforming_factory, aggressive_s)
    ]

    tournament_begin(
        tournament_second,
        "2 (multiple)",
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )


if __name__ == "__main__":
    main()
