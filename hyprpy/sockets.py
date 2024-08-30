from typing import Callable, Final

import os
import pathlib
import asyncio


_WRITE_SOCKET_FILENAME: Final[str] = ".socket.sock"
_READ_SOCKET_FILENAME: Final[str] = ".socket2.sock"

_XDG_RUNTIME_DIR_KEY: Final[str] = "XDG_RUNTIME_DIR"
_HYPRLAND_INSTANCE_SIGNATURE: Final[str] = "HYPRLAND_INSTANCE_SIGNATURE"

_SOCKET_SUB_DIR: Final[str] = "hypr"

async def _get_env[T](env_key: str, default: T = None) -> str | T:
    value = os.getenv(env_key) # Missing key results in None
    return default if value is None else value

def _hypr_sock_path(xdg_runtime_dir: str, hyprland_instance_signature: str) -> pathlib.Path:
    path: str = os.path.join(xdg_runtime_dir, _SOCKET_SUB_DIR, hyprland_instance_signature)
    return pathlib.Path(path)

def _liftA2[A, B, C](f: Callable[[A, B], C], a: A | None , b: B | None) -> C | None:
    if a is None or b is None:
        return None
    return f(a, b)

async def get_hypr_socket_dir() -> pathlib.Path | None:
    xdg_runtime_dir_task = _get_env(_XDG_RUNTIME_DIR_KEY)
    hyprland_instance_signature_task = _get_env(_HYPRLAND_INSTANCE_SIGNATURE)
    xdg_runtime_dir, hyprland_instance_signature = await asyncio.gather(
            xdg_runtime_dir_task,
            hyprland_instance_signature_task
    )
    return _liftA2(_hypr_sock_path, xdg_runtime_dir, hyprland_instance_signature)


