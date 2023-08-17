'''Task 2:
1)You have a football field that is 92 meter long and 48.8 meter wide.
Find out total area using python and print it.
'''
length=92
width=48.8
total_area=length*width
print(total_area)


'''
2)You bought 9 packets of potato chips from a store.Each packet costs 1.49 dollar
and you gave shopkeeper 20 dollar.Find out using python,how many dollars is
the shopkeeper going to give you back?
'''
chips_rate=1.49
total_brought=9*1.49
given=20
print("Shop keeper should give you:",given-total_brought)

#output:Shop keeper should give you: 6.59

'''
3)You want to replace tiles in your bathroom which is exactly square and 5.5
feet is its length. If tiles cost 500 rs per square feet, how much will be the
total cost to replace all tiles. Calculate and print the cost using python
(Hint: Use power operator ** to find area of a square)
'''

length=5.5
total_sqr_feet=5.5**2
total_cost=500*total_sqr_feet
print("Total cost to replace all tiles is:",total_cost)


#output:Total cost to replace all tiles is: 15125.0

'''
4)Print binary representation of number 17
'''
n=17
print(format(n,'b'))

#output:10001
