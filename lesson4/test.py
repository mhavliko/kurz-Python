seznam = ['12.03.2014', '10.01.2015', '06.06.1986']
seznam1 = [int(datum[3:5]) for datum in seznam]
seznam1 = [int(datum[:2])-1 for datum in seznam]
seznam1 = [[int(datum[:2]), int(datum[3:5]), int(datum[6:])] for datum in seznam]
seznam1 =[datum.split('.') for datum in seznam]
seznam1 =['/'.join(datum.split('.')) for datum in seznam]

print (seznam1)
