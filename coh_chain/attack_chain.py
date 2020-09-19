from coh_chain.powersets import brute_ss, stalker_elec_shield
from coh_chain.globals import get_globals

SIM_TIME = 180

class AttackChain:

    def __init__(self, powers, sim_time=SIM_TIME):
        self._globals = get_globals()

        self.total_damage = 0.0
        self.time_elapsed = 0.0
        self.current_end = self._globals.total_end
        self.sim_time = sim_time

        self.powers_by_dpa = sorted(powers, key=lambda x: x.dpa, reverse=True)

    def start(self):

        print("\n")
        print("Powers with Damage per Animation")
        print("--------------------------------")
        for power in self.powers_by_dpa:
            print(", ".join([power.name, str(power.dpa)]))
        print("--------------------------------")
        print("\n")

        while self.time_elapsed < self.sim_time:
            power = self.get_next_power()
            if power.endurance > self.current_end:
                self.pp("OUT OF ENDURANCE!!!")
                break

            # Activate power
            self.total_damage += power.total_damage
            power.damage_delivered += power.total_damage
            power.activation_count += 1
            # Remove endurance for the power immediately
            self.current_end -= power.endurance

            cooldown_powers = ", ".join([x.name for x in self.powers_by_dpa if x.is_ready is False])
            self.pp(f"Activated {power.name} ({power.activation_count}) hitting {power.mobs_hit} mobs for {power.total_damage:.2f} total dmg --- (Cooldown: {cooldown_powers})")

            self.pass_time(power.animation)
            power.on_cooldown()


        print(f"Total Time Elapsed {self.time_elapsed}")
        print(f"Total Damage {self.total_damage} / DPS {self.total_damage / self.time_elapsed}")

        print("\n")
        print("Power, Activation Count, Total Dmg, Dmg/s, Total Endurance Cost")
        print("--------------------------------")
        # Sort by total damage delivered
        for power in sorted(self.powers_by_dpa, key=lambda x: x.damage_delivered, reverse=True):
            print(
                ", ".join([
                    power.name,
                    f"{power.activation_count}",
                    f"{power.damage_delivered:.2f}",
                    f"{power.damage_delivered / self.time_elapsed:.2f}/sec",
                    f"{power.activation_count * power.endurance:.2f}"
                ])
            )
        print("--------------------------------")
        print("\n")

    def pp(self, string):
        print(f"[{self.time_elapsed:4.2f}] ({self.current_end:3.2f} end) {string}")

    def get_next_power(self):
        next_power = None
        for power in sorted(self.powers_by_dpa, key=lambda x: x.dpa_with_cooldown, reverse=True):
            if power.is_ready:
                next_power = power
                break
            elif next_power is None or power.cooldown < next_power.cooldown:
                next_power = power

        if next_power.cooldown > 0:
            self.pp(f"WAITING {next_power.cooldown} seconds for an available power!")
            self.pass_time(next_power.cooldown)
        return next_power

    def pass_time(self, time):
        self.time_elapsed += time

        # Update the cooldowns for all powers
        for power in self.powers_by_dpa:
            power.pass_time(time)

        # Then add any end that was gained due to base recovery
        self.current_end += time * self._globals.base_end_recovery

        # Remove end drain from base drain (toggles)
        self.current_end -= time * self._globals.base_end_drain


if __name__ == '__main__':
    AttackChain().start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
