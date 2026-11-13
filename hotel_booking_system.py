
"""Hotel room reservation and booking management module."""

import hashlib
import secrets

room_inventory = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Reserve an available room for a guest."""
    if booking_log is None:
        booking_log = []

    if room_num not in room_inventory:
        return False

    if room_inventory[room_num]["is_booked"]:
        return False

    room_inventory[room_num]["is_booked"] = True
    booking_log.append(
        f"Reserved room {room_num} for guest {guest_name}"
    )
    return True


def cancel_booking(room_num):
    """Cancel an existing room reservation."""
    if room_num not in room_inventory:
        return False

    room_inventory[room_num]["is_booked"] = False
    return True


def check_room_status(room_num):
    """Return whether a room exists and is available."""
    return (
        room_num in room_inventory
        and not room_inventory[room_num]["is_booked"]
    )


def compute_seasonal_rate(room_num, multiplier):
    """Calculate a room's price using a seasonal multiplier."""
    if room_num not in room_inventory:
        raise ValueError("Room does not exist")

    if multiplier <= 0:
        raise ValueError("Multiplier must be greater than zero")

    base_price = room_inventory[room_num]["price"]
    return base_price * multiplier


def generate_guest_hash(guest_id):
    """Generate a SHA-256 hash for a guest identifier."""
    return hashlib.sha256(guest_id.encode("utf-8")).hexdigest()


def generate_booking_ref():
    """Generate a secure booking reference number."""
    return secrets.randbelow(9000) + 1000


def export_room_ledger(filename="hotel_ledger.txt"):
    """Export the current room inventory to a text file."""
    with open(filename, "w", encoding="utf-8") as ledger_file:
        ledger_file.write(str(room_inventory))

    print("Hotel ledger exported to:", filename)


def main():
    """Run the hotel booking system demonstration."""
    book_room("101", "Emma Watson")
    cancel_booking("102")

    print("Is 103 available:", check_room_status("103"))
    print("Surge price:", compute_seasonal_rate("101", 1.25))
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())

    export_room_ledger()


if __name__ == "__main__":
    main()
