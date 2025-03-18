"""This is where the server gets its recieved keys from."""
import keyboard

def get_keys(e: keyboard.KeyboardEvent) -> str:
    """This gets any single key or key combination until those keys are released."""
    keys = set()
    while True:
        if e.event_type == keyboard.KEY_DOWN:
            keys.add(e.name)
        if keyboard.read_event() == keyboard.KEY_UP:
            return "+".join(keys)
