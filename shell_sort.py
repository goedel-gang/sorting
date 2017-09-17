GAPS = [701, 301, 132, 57, 23, 10, 4, 1]

def shell_sort(l):
    for gap in GAPS:
        for i in xrange(len(l)):
            yield i,
            for j in xrange(i, gap - 1, -gap):
                yield j, j - gap
                if l[j] < l[j - gap]:
                    yield j, j - gap
                    l[j], l[j - gap] = l[j - gap], l[j]
                else:
                    break
