import asyncio
from unittest import result

from fetch_data import fetch_data
from prepare_coin_base_data import prepare_coin_base_data
from prepare_gemini_data import prepare_gemini_data
from bitcoins_paid import bitcoins_paid
coin_base_file_url = "https://api.exchange.coinbase.com/products/BTC-USD/book?level=2"
gemini_file_url = "https://api.gemini.com/v1/book/BTCUSD"


async def get_data_in_one_cycle(number_bitcoins: float) -> tuple[float, float]:
    coin_base_data = await fetch_data(coin_base_file_url)
    asks_coin_base_result = prepare_coin_base_data(coin_base_data, False)
    bids_coin_base_result = prepare_coin_base_data(coin_base_data, True)

    gemini_data = await fetch_data(gemini_file_url)
    asks_gemini_result = prepare_gemini_data(gemini_data, False)
    bids_gemini_result = prepare_gemini_data(gemini_data, True)

    all_asks = asks_coin_base_result + asks_gemini_result
    all_sorted_asks = sorted(all_asks, key=lambda x: x[0], reverse=False)
    total_cost_to_buy = bitcoins_paid(all_sorted_asks,number_bitcoins)

    all_bids = bids_coin_base_result + bids_gemini_result
    all_sorted_bids = sorted(all_bids, key=lambda x: x[0], reverse=True)
    total_cost_to_sell = bitcoins_paid(all_sorted_bids, number_bitcoins)

    return [total_cost_to_buy, total_cost_to_sell]

async def do_one_cycle(number_bitcoins: float):
    result = await get_data_in_one_cycle(number_bitcoins)
    print("\n\n--------------------------------------")
    print(f"To buy {number_bitcoins} BTC: ${result[0]:,.2f}")
    print(f"To sell {number_bitcoins} BTC: ${result[1]:,.2f}")


async def do_cycles(number_bitcoins: float) :
    while True:
        await do_one_cycle(number_bitcoins)
        await asyncio.sleep(2)

async def main(argv):
    if (len(argv) > 2 and argv[1]=="-qty" and argv[2].isnumeric()):
        number_bitcoins = float(argv[2])
    else:
        number_bitcoins = 10

    await do_cycles(number_bitcoins)


if __name__ == "__main__":
    asyncio.run(main(argv=asyncio.sys.argv))