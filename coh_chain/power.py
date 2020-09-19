from .globals import get_globals

class Power:

    def __init__(self, name, damage, recharge, animation, endurance, max_mobs, immutable_recharge=False):
        self.name = name
        self.damage = damage
        self.recharge = recharge
        self.animation = animation
        self.endurance = endurance
        self.max_mobs = max_mobs
        self.cooldown = 0.0
        self._globals = get_globals()
        self.damage_delivered = 0.0
        self.activation_count = 0
        self.immutable_recharge = immutable_recharge

    def on_cooldown(self):
        if self.immutable_recharge:
            self.cooldown = self.recharge
        else:
            self.cooldown = self.recharge / self._globals.recharge_modifier

    @property
    def is_ready(self):
        if self.cooldown <= 0.0:
            return True

        return False

    def pass_time(self, time):
        self.cooldown -= time
        if self.cooldown < 0:
            self.cooldown = 0

    @property
    def mobs_hit(self):
        if self.max_mobs < self._globals.mob_count:
            return self.max_mobs
        else:
            return self._globals.mob_count

    @property
    def dpa(self):
        return self.damage * self._globals.damage_modifier * self.mobs_hit / self.animation

    @property
    def dpa_with_cooldown(self):
        # return self.damage * self._globals.damage_modifier * self.mobs_hit / (self.animation + self.cooldown)
        return self.damage * self._globals.damage_modifier * self.mobs_hit / self.animation


    @property
    def total_damage(self):
        return self.damage * self._globals.damage_modifier * self.mobs_hit
