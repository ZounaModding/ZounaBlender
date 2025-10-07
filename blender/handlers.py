from enum import Enum
from typing import Callable, Dict, Tuple

# A global registry of handlers
# key is (Platform, version_str, member_name)
Handler = Callable[[object], None]
_handlers: Dict[Tuple[Enum, str, str], Handler] = {}


def make_handler(version_class, platform, version_str, member_name):
    """
    Helper function called for each combination to automatically generate a handler.
    """

    @register_handler(platform, version_str, member_name)
    def handler(bff_class):
        return version_class(bff_class).to_generic()

    return handler


def register_handler(
    platform: Enum, version: str, member_name: str
) -> Callable[[Handler], Handler]:
    """
    Decorator to register a handler for a specific (platform, version, member_name).
    The handler will be called with the *value* of that member.
    """

    def decorator(fn: Handler) -> Handler:
        key = (platform, version, member_name)
        if key in _handlers:
            raise KeyError(f"Handler already registered for {key!r}")
        _handlers[key] = fn
        return fn

    return decorator


def get_handler(platform: Enum, version: str, member_name: str) -> Handler | None:
    """
    Obtain a handler for the given combination.
    """
    return _handlers.get((platform, version, member_name))
