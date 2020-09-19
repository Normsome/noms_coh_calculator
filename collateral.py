from coh_chain.globals import init_globals
from coh_chain.powersets import stalker_elec_shield
from coh_chain.attack_chain import AttackChain

if __name__ == "__main__":
    init_globals(
        mob_count=1,
        damage_modifier=1.0,
        base_end_recovery=100.0,
        base_end_drain=0.52,
        total_end=105.0,
        recharge_modifier=3.15,
    )
    AttackChain(powers=stalker_elec_shield.load_powers()).start()