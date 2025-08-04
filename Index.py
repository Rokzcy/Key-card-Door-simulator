# Simulated database of authorized key card IDs
authorized_cards = {
    "CARD1234": "Alice",
    "CARD5678": "Bob",
    "CARD9012": "Charlie"
}

def check_access(card_id):
    """
    Checks if the provided card ID is in the authorized list.
    """
    if card_id in authorized_cards:
        user = authorized_cards[card_id]
        print(f"Access Granted: Welcome, {user}!")
        return True
    else:
        print("Access Denied: Unauthorized Card.")
        return False

# Example usage
if __name__ == "__main__":
    # Simulate scanning a card
    scanned_card = input("Please scan your card (enter card ID): ").strip()
    check_access(scanned_card)
