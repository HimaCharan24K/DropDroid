import json
from pathlib import Path
from enum import Enum


class EpisodeState(Enum):
    PENDING = "PENDING"

    DOWNLOADING = "DOWNLOADING"

    VERIFYING = "VERIFYING"

    SENDING = "SENDING"

    DELIVERED = "DELIVERED"

    WAITING_FOR_DONE = "WAITING_FOR_DONE"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    RECOVERED = "RECOVERED"

    SKIPPED = "SKIPPED"

    DEAD = "DEAD"


VALID_TRANSITIONS = {
    EpisodeState.PENDING: [
        EpisodeState.DOWNLOADING
    ],

    EpisodeState.DOWNLOADING: [
        EpisodeState.VERIFYING,
        EpisodeState.FAILED
    ],

    EpisodeState.VERIFYING: [
        EpisodeState.SENDING,
        EpisodeState.FAILED
    ],

    EpisodeState.SENDING: [
        EpisodeState.DELIVERED,
        EpisodeState.FAILED
    ],

    EpisodeState.DELIVERED: [
        EpisodeState.WAITING_FOR_DONE
    ],

    EpisodeState.WAITING_FOR_DONE: [
        EpisodeState.COMPLETED,
        EpisodeState.SKIPPED
    ],

    EpisodeState.FAILED: [
        EpisodeState.RECOVERED,
        EpisodeState.DEAD
    ],

    EpisodeState.RECOVERED: [
        EpisodeState.DOWNLOADING
    ]
}

def can_transition(current_state, next_state):
    allowed_states = VALID_TRANSITIONS.get(current_state, [])

    return next_state in allowed_states

STATE_FILE = Path("state.json")
BACKUP_FILE = Path("state.backup.json")
TEMP_FILE = Path("state.tmp")

def load_state():
    if not STATE_FILE.exists():
        return {}

    with open(STATE_FILE, "r") as file:
        return json.load(file)

def save_state(data):

    with open(TEMP_FILE, "w") as file:
        json.dump(data, file, indent=4)

    with open(TEMP_FILE, "r") as file:
        json.load(file)

    if STATE_FILE.exists():
        with open(STATE_FILE, "r") as source:
            with open(BACKUP_FILE, "w") as backup:
                backup.write(source.read())

    TEMP_FILE.replace(STATE_FILE)

def restore_backup():

    if not BACKUP_FILE.exists():
        return False

    BACKUP_FILE.replace(STATE_FILE)

    return True
