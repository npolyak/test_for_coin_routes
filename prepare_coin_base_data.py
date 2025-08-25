from to_float import to_float

def prepare_coin_base_data(data, bidsOrAsks: bool):
    prop_name = 'bids' if bidsOrAsks else 'asks'

    # Remove rows without 2 values
    remove_rows_without_2_values_result = filter(lambda x: len(x) >= 2, data[prop_name])

    # Convert to float and filter out None values
    result = list(filter(lambda x: x[0] != None and x[1] != None, map(lambda x: [to_float(x[0]),  to_float(x[1])], remove_rows_without_2_values_result)))

    return result

