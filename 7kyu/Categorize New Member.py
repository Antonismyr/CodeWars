def open_or_senior(data):
    return ['Senior' if age >= 55 and hand > 7 else 'Open' for age, hand in data]