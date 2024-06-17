persons = [('Lisboa', 'LIS', 'DHR'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destiny = 'FCO'
fligths = {}

for line in open('../../data/flights.txt'):
    origin, destiny, departure, arrival, price = line.split(',')
    fligths.setdefault((origin, destiny), [])
    fligths[(origin, destiny)].append((departure, arrival, int(price)))

print(fligths)
