def john_mary(str):
    words = set(str.split('&'))
    counts = {}
    for word in words:
        counts[word] = str.count(word)

    return len(set(counts.values())) < 2

print(john_mary('John&Mary'))
print(john_mary('John&John&Mary'))
print(john_mary('John&John&John&Mary&Mary'))
print(john_mary('John&John&John&Mary&Mary&Mary'))
