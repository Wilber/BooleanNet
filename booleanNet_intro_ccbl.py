import boolean2
from boolean2 import Model



#specify rules: an initial state and updating rules 

text = """
#A = B = C = True 
A = False
B = C = True 

A* = A or not C
B* = A and C
C* = B

"""

#Model creation, a synchronized updating scheme 
model = boolean2.Model(text, mode='sync')
model.initialize()

#model evolution 
model.iterate( steps=5 )
for state in model.states:
    print state

#Cycle detection
#size, index = model.detect_cycles()    
#print "Size =%s, Index %s" % (size, index)

model.report_cycles()


##State modification: specifying gene deletion(s) and observing the change in attractors
on = ["A", "B"]
off = ["C"]
new_text = boolean2.modify_states(text, turnon=on, turnoff=off) ##need to upload rules from a text file?


model = boolean2.Model(new_text, mode='sync')
model.initialize()

#model evolution 
model.iterate( steps=5 )
for state in model.states:
    print state

#Cycle detection- detecting attractors
model.report_cycles()
