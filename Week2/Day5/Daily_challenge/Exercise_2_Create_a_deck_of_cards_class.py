import random
from typing import List, Optional, Tuple

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"

    def to_tuple(self) -> Tuple[str, str]:
        return (self.value, self.suit)

class Deck:
    
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.cards: List[Card] = []
        self._initialize_deck()
        self.shuffle()
        print(f"✅ Deck created and shuffled. Cards in deck: {len(self.cards)}")

    def _initialize_deck(self):
        self.cards = []
        for suit in self.SUITS:
            for value in self.VALUES:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        if len(self.cards) != 52:
            print("⚠️ Deck is incomplete. Creating a new full deck before shuffling.")
            self._initialize_deck()
            
        random.shuffle(self.cards)
        print("🔀 Deck successfully shuffled.")
        
    def deal(self) -> Optional[Card]:
        if not self.cards:
            print("❌ Deck is empty, nothing to deal.")
            return None
        
        return self.cards.pop()

if __name__ == "__main__":
    
    print("\n--- DECK CLASS DEMONSTRATION START ---")
    
    my_deck = Deck()
    
    print(f"Initial number of cards: {len(my_deck.cards)}")
    
    print("\nDealing five cards:")
    dealt_cards = []
    for i in range(5):
        card = my_deck.deal()
        if card:
            dealt_cards.append(card)
            print(f"  Card {i+1}: {card}")
            
    print(f"\nNumber of cards after dealing: {len(my_deck.cards)}")

    print("\n--- RESHUFFLING ---")
    my_deck.shuffle()
    
    next_card = my_deck.deal()
    if next_card:
        print(f"\nNext card after shuffling: {next_card}")
    
    print(f"Final number of cards: {len(my_deck.cards)}")
    
    print("\n--- EMPTYING THE DECK (for test) ---")
    
    while my_deck.cards:
        my_deck.cards.pop()
        
    print(f"Deck emptied. Cards: {len(my_deck.cards)}")
    
    empty_deal = my_deck.deal()
    if empty_deal is None:
        print("✅ Check: Dealing from an empty deck works (returns None).")

    print("\n--- TEST: SHUFFLE with an empty deck ---")
    my_deck.shuffle()
    print(f"Number of cards after 'shuffle' on empty deck: {len(my_deck.cards)}")