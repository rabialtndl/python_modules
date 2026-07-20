import abc
from ex0.Abstract_Factory import Creature


class StrategyError(Exception):
    pass


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if hasattr(creature, "transform") and hasattr(creature, "revert"):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        print(creature.transform())  # type: ignore
        print(creature.attack())
        print(creature.revert())  # type: ignore


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if hasattr(creature, "heal"):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'"
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())  # type: ignore
