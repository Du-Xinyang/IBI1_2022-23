# write	a	function	which	determines	whether an	individual	can buy	a	specific	house.
# This	 function	should	take two	parameters:	 (1)	the	 total	value	 of	 the	house and (2)	the	purchaser’s	 annual	 salary.
def f(x,y):

    if x <= 5*y:
        print('Yes')
    else:
        print('No')
value = 180000
salary = 35000

# there	is	an	example	function	call	contained	within	this	script.
f(value,salary)
