import sys
from typing import Tuple


def get_platform() -> Tuple[str, int]:
    bits = 64 if sys.maxsize > 2 ** 32 else 32
    platforms = {
        "linux": "Linux",
        "linux1": "Linux",
        "linux2": "Linux",
        "darwin": "OS X",
        "win32": "Windows",
    }
    if sys.platform not in platforms:
        return sys.platform, bits

    return platforms[sys.platform], bits
