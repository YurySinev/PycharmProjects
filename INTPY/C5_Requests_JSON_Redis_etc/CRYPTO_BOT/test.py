keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'solana': 'SOL',
    'доллар': 'USDT'
}

def values():
    text = 'Доступные валюты:'
    for k in keys.keys():
        text = '\n'.join((text, k))
    print(text)

values()

