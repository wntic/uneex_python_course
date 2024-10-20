from collections import defaultdict


def get_data() -> tuple[defaultdict]:
    decks = defaultdict(set)
    players = defaultdict(list)

    while True:
        line = input()
        if not line:
            break

        data = line.split(" / ")
        if data[0].isdigit():
            deck_num = data[0]
            card_name = data[1]
            decks[deck_num].add(card_name)
        else:
            player_name = data[0]
            deck_num = data[1]
            players[player_name].append(deck_num)

    return players, decks


def pokemon(players, decks) -> list[str]:
    cards_count = {}

    for player, deck_nums in players.items():
        unique_cards = set()
        for deck_num in deck_nums:
            unique_cards.update(decks[deck_num])
        cards_count[player] = len(unique_cards)

    if cards_count:
        max_pack_size = max(cards_count.values())
    else:
        max_pack_size = 0

    top_players = [
        player for player, count in cards_count.items() if count == max_pack_size
    ]
    return sorted(top_players)


if __name__ == "__main__":
    players, decks = get_data()
    result = pokemon(players, decks)
    print("\n".join(r for r in result))
