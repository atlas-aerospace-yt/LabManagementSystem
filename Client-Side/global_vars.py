"""
Global variables that can change are defined here.
"""

from connection_manager import ConnectionManager

try:
    CONNECTION_MANAGER = ConnectionManager()
except ConnectionRefusedError:
    CONNECTION_MANAGER = None

USER_ID = None
USER_EMAIL = None
LOGGED_IN = False

PRIORITY = -1

def get_first_id(query:str) -> int:
    """
    Get the first available Primary key that can be used to insert a new record.

    Args:
        query(str): The query that selects the primary keys that already exist.

    Returns:
        int: the first available booking ID.
    """
    booking_ids = CONNECTION_MANAGER.send_command(query)
    ordered_ids = sorted([int(i[0]) for i in booking_ids])
    used_id = ordered_ids[0]

    if used_id == 0:
        for booking_id in ordered_ids[1:]:
            if used_id+1 != booking_id:
                return used_id+1
            used_id += 1
    else:
        return 0
    return used_id+1
