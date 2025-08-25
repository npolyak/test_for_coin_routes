from to_float import to_float

def prepare_gemini_data(data, bidsOrAsks: bool):
    prop_name = 'bids' if bidsOrAsks else 'asks'
    data = data[prop_name]

    gemini_result = list(filter(lambda x: x[0] is not None and x[1] is not None, map(lambda x: [to_float(x['price']), to_float(x['amount'])], data)))

    return gemini_result

