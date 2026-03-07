
DEX_PRIORITY = ["dedust", "ston"]

SEEN_TX = set()

def choose_dex(token_settings):
    override = token_settings.get("dex_override")
    if override in ("dedust","ston"):
        return override
    for d in DEX_PRIORITY:
        return d

def is_duplicate(tx_hash, amount, token):
    key = f"{tx_hash}:{amount}:{token}"
    if key in SEEN_TX:
        return True
    SEEN_TX.add(key)
    return False
