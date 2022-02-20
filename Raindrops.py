def convert(number, raindrops=((3, 'Pling'),(5, 'Plang'), (7, 'Plong'))):

    return ''.join(v * (not number % k) for k, v in raindrops) or str(number)
