_GLOBALS = None


class Globals:
    def __init__(self, mob_count=1, damage_modifier=1.0, total_end=100, base_end_recovery=1.0, base_end_drain=0.0,
                 recharge_modifier=1.0):
        self.mob_count = mob_count
        self.damage_modifier = damage_modifier
        self.total_end = total_end
        self.base_end_recovery = base_end_recovery
        self.base_end_drain = base_end_drain
        self.recharge_modifier = recharge_modifier


def init_globals(*args, **kwargs) -> Globals:
    global _GLOBALS
    _GLOBALS = Globals(*args, **kwargs)
    return _GLOBALS


def get_globals() -> Globals:
    if _GLOBALS is None:
        raise RuntimeError("Globals have not yet been initialized")
    return _GLOBALS
