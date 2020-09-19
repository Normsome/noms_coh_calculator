from coh_chain.power import Power


def load_powers():
    punch = Power(
        name="Punch",
        damage=84.62362,
        recharge=1.256627,
        animation=1.452,
        endurance=2.819383,
        max_mobs=1
    )

    haymaker = Power(
        name="Haymaker",
        damage=142.1814,
        recharge=2.699625,
        animation=1.716,
        endurance=3.557502,
        max_mobs=1
    )

    knockout_blow = Power(
        name="Knockout Blow",
        damage=470.3312,
        recharge=8.822232,
        animation=2.376,
        endurance=9.523858,
        max_mobs=1
    )

    hurl = Power(
        name="Hurl",
        damage=144.5904,
        recharge=2.758621,
        animation=2.64,
        endurance=4.395398,
        max_mobs=1
    )

    foot_stomp = Power(
        name="Foot Stomp",
        damage=177.8769,
        recharge=6.376026,
        animation=2.244,
        endurance=11.48031,
        max_mobs=10
    )
    spring_attack = Power(
        name="Spring Attack",
        damage=289.7663,
        recharge=44.20704,
        animation=1.716,
        endurance=7.410249,
        max_mobs=5
    )

    judgement_void = Power(
        name="Void Radial Final Judgement",
        damage=456.2021,
        recharge=90,
        animation=2.244,
        endurance=17.2043,
        max_mobs=10,
        immutable_recharge=True
    )

    toxic_dart = Power(
        name="Toxic Dart",
        damage=114.87,
        recharge=1.429763,
        animation=1.32,
        endurance=4.971391,
        max_mobs=1,
    )

    laser_beam = Power(
        name="Laser Beam Eyes",
        damage=86.69597,
        recharge=1.877053,
        animation=1.848,
        endurance=3.081481,
        max_mobs=1,
    )

    arcane_bolt = Power(
        name="Arcane Bolt",
        damage=95.69002,
        recharge=1.668057,
        animation=2.244,
        endurance=3.648474,
        max_mobs=1,
    )

    cross_punch = Power(
        name="Cross Punch",
        damage=119.4,
        recharge=2.98,
        animation=1.848,
        endurance=4.81,
        max_mobs=3,
    )

    all_powers = [
        punch,
        haymaker,
        knockout_blow,
        #hurl,
        foot_stomp,
        #spring_attack,
        judgement_void,
        #toxic_dart,
        laser_beam,
        #arcane_bolt,
        #cross_punch,
    ]

    return all_powers
