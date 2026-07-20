from ex0 import AquaFactory, FlameFactory, CreatureFactory


def TestFactory(factory: CreatureFactory) -> None:
    print("\nTesting factory")
    factory_base = factory.create_base()
    print(factory_base.describe())
    print(factory_base.attack())

    factory_evolved = factory.create_evolved()
    print(factory_evolved.describe())
    print(factory_evolved.attack())


def TestBattle(Fighter1: CreatureFactory, Fighter2: CreatureFactory) -> None:
    print("\nTesting battle")
    Fighter1_base = Fighter1.create_base()
    Fighter2_base = Fighter2.create_base()
    print(Fighter1_base.describe())
    print(" vs.")
    print(Fighter2_base.describe())
    print(" fight!")
    print(Fighter1_base.attack())
    print(Fighter2_base.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    TestFactory(flame_factory)
    TestFactory(aqua_factory)
    TestBattle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
