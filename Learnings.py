Learnings:

tuples vs lists:
tuples cannot be extended or shortened. Its static
But tuples are faster to traverse.


Using Generators dont have to store things in memory
Generator: A function that yeilds result: Then run another loop using that genrator to throw final values

Generator(throws one value at a time.) No extra memory usage. No time to buld a generator but data is also not there.
When you loop: ok When you mak list: same time and memory as list comprehension.


zip(list1, list2): gives list of tuples. dict(zip(l1,l2)) gives dictionary

enumerate(dictionary) gives tuple of key and value
enumerate(list) gives a tuple of index and value

map iterates over a iterable.
map(func, list) == [func(i) for i in list]
func can be implemented by lambda or defining a function earlier:
map(lambda x: x**3, list)
if two iterators in args apart from the func func takes 2 args, in sequence
eg: map(pow, l1, l2)

filter(aFunction, aSequence) filter the iterable based on normal func or lambda func
reduce(aFunction, aSequence) lakes iterator, returns single, like add strings to return one string
eg: reduce((lambda x, y: x / y), [1, 2, 3, 4])


itertools.count(a, b) >> start from a, steps of b
itertools.chain(p, q ..) > p0,p1..,q0,q1...
itertools.combinations(iterable, n) >> combinations of iterable, len(it)Cn
itertools.groupby(iterator, key=lambda func or something)>> returns key, group where group  is a groupby object