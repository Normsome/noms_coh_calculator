from coh_chain.globals import init_globals
from coh_chain.attack_chain import AttackChain
from coh_chain.powersets import brute_ss

if __name__ == "__main__":
    print("Stats for Kremlin")
    init_globals(
        mob_count=1,
        damage_modifier=2.35,
        base_end_recovery=3.65,
        base_end_drain=0.65,
        total_end=107.1,
        recharge_modifier=1.0,
    )
    AttackChain(sim_time=300, powers=brute_ss.load_powers()).start()
