from coh_chain.power import Power


def load_powers():
    charged_brawl = Power(
        name="Charged Brawl",
        damage=49.98,
        recharge=3.00,
        animation=0.83,
        endurance=4.37,
        max_mobs=1
    )

    havoc_punch = Power(
        name="Havoc Punch",
        damage=78.54,
        recharge=6.00,
        animation=1.50,
        endurance=6.86,
        max_mobs=1
    )

    jacobs_ladder = Power(
        name="Jacobs Ladder",
        damage=89.25,
        recharge=8.00,
        animation=1.67,
        endurance=8.53,
        max_mobs=3
    )

    zapp = Power(
        name="Zapp",
        damage=313.31,
        recharge=24.00,
        animation=1.00,
        endurance=17.94,
        max_mobs=1
    )

    chain_induction = Power(
        name="Chain Induction",
        damage=234.25,
        recharge=14.00,
        animation=1.00,
        endurance=10.19,
        max_mobs=4
    )
    assassin_shock = Power(
        name="Assassin Shock",
        damage=148.76,
        recharge=15.00,
        animation=1.00,
        endurance=14.35,
        max_mobs=1
    )

    spring_attack = Power(
        name="Spring Attack",
        damage=83.42,
        recharge=120,
        animation=1.50,
        endurance=13.52,
        max_mobs=5
    )

    ball_lightning = Power(
        name="Ball Lightning",
        damage=60.69,
        recharge=32.00,
        animation=1.07,
        endurance=18.98,
        max_mobs=10
    )

    shield_charge = Power(
        name="Shield Charge",
        damage=141.81,
        recharge=90,
        animation=1.50,
        endurance=13.52,
        max_mobs=10
    )

    thunder_strike = Power(
        name="Thunder Strike",
        damage=116.63,
        recharge=18,
        animation=3.30,
        endurance=18.00,
        max_mobs=5
    )

    lightning_rod = Power(
        name="Lightning Rod",
        damage=177.67,
        recharge=90,
        animation=2.57,
        endurance=13.52,
        max_mobs=10
    )

    pyronic_core = Power(
        name="Pyronic Core",
        damage=491.57,
        recharge=90,
        animation=1.00,
        endurance=20.00,
        max_mobs=10,
        immutable_recharge=True,
    )

    all_powers = [
        charged_brawl,
        havoc_punch,
        jacobs_ladder,
        zapp,
        chain_induction,
        assassin_shock,
        spring_attack,
        ball_lightning,
        shield_charge,
        thunder_strike,
        lightning_rod,
        pyronic_core
    ]

    return all_powers
