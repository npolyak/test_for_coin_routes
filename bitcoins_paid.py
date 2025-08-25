import json

def bitcoins_paid(all_sorted : list[tuple[float, float]], number_bitcoins : float) -> float:
    total_bitcoins = 0.
    total_payed = 0.
    for entry in all_sorted:
        left_over = number_bitcoins - total_bitcoins

        bit_coins_from_current_entry = entry[1]
        if (left_over < bit_coins_from_current_entry):
            bit_coins_from_current_entry = left_over

        total_bitcoins += bit_coins_from_current_entry

        total_payed += entry[0] * bit_coins_from_current_entry

        if (total_bitcoins >= number_bitcoins):
            break
    return total_payed
