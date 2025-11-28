def convert(sec):
    min = sec // 60
    remainingSec = sec % 60
    hr = min // 60
    min = min % 60
    return [hr, min, remainingSec]


