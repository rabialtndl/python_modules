from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    if hasattr(base, 'heal'):
        print(base.heal())  # type: ignore

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())

    if hasattr(evolved, 'heal'):
        print(evolved.heal())  # type: ignore


def test_transforming(factory: TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    if hasattr(base, "transform") and hasattr(base, "revert"):
        print(base.transform())  # type: ignore
        print(base.attack())
        print(base.revert())  # type: ignore

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())

    if hasattr(evolved, "transform") and hasattr(evolved, "revert"):
        print(evolved.transform())  # type: ignore
        print(evolved.attack())
        print(evolved.revert())  # type: ignore


def main() -> None:
    heal_factory = HealingCreatureFactory()
    test_healing(heal_factory)
    tranform_factory = TransformCreatureFactory()
    test_transforming(tranform_factory)


if __name__ == "__main__":
    main()
