kurz = {
  'nazev': 'Úvod do programování',
  'lektor': 'Martin Podloucký',
  'konani': [
    {
      'misto': 'T-Mobile',
      'koucove': [
        'Dan Vrátil',
        'Filip Kopecký',
        'Martina Nemčoková'
      ],
      'ucastnic': 30
    },
    {
      'misto': 'MSD IT',
      'koucove': [
        'Dan Vrátil',
        'Zuzana Tučková',
        'Martina Nemčoková'
      ],
      'ucastnic': 25
    },
    {
      'misto': 'Škoda DigiLab',
      'koucove': [
        'Dan Vrátil',
        'Filip Kopecký',
        'Kateřina Kalášková'
      ],
      'ucastnic': 41
    }
  ]
}

print(len(kurz['konani']))
mista = [misto['misto']for misto in kurz['konani']]
print(mista)
