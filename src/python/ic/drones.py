

def find_unique(ids):
    unique_delivery_id = 0

    for id in ids:
        unique_delivery_id ^= id

    return unique_delivery_id
