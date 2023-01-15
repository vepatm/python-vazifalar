countries = ['Uzbekistan', 'Turkmenistan', 'Russia', 'USA', 'UK']
print(len(countries))

print(sorted(countries))
print(sorted(countries, reverse=True))

print(countries)
countries.reverse()
print(countries)

countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

juft_sonlar = list(range(120,1200,2))
print(sum(juft_sonlar))
print(max(juft_sonlar) - min(juft_sonlar))
print(len(juft_sonlar))
print(juft_sonlar[0:20])
print(juft_sonlar[520:])
print(juft_sonlar[261:281])

taomlar = ['osh', 'manti', 'somsa', 'chuchvara', 'sariyog\'', 'tuxum']
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove('manti')
nonushta.remove('somsa')
nonushta.remove('chuchvara')
nonushta.append('asal')
nonushta.append('murabbo')
print(taomlar)
print(nonushta)

nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'
print(nonushta)  # TypeError: 'tuple' object does not support item assignment