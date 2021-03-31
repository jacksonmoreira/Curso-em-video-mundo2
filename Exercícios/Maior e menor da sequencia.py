# Exercise 054
print('{:#^60}'.format(' Bigger and smaller of the sequence '))
biggest= 0
smallest = 0
for a in range(1, 6):
    weight = float(input('Insert the {}° person weight: '.format(a)))
    if a == 1:
        biggest = weight
        smallest = weight
    else:
        if weight > biggest:
            biggest = weight
        if weight < smallest:
            smallest = weight
print('Biggest weight {}kg!\nSmallest weight {}kg!'.format(biggest, smallest))
