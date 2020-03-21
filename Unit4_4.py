stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
print(max(list(stats.values())))

inverse = [(value, key) for key, value in stats.items()]

#print(inverse)

print(max(inverse)[1])