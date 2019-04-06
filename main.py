from time import sleep

#put your derivaitve from https://www.symbolab.com/solver/tangent-to-conic-calculator/derivative here
def derivative(x):
    return 2*x+3
def calc_tangent(x,gradient):
    #rearnagement of y=mx+c to give c
    c=function(x)-gradient*x
    return c
#put the fucntion you are decending here
def function(x):
    return x*x+3*x

#set your learning rate here
lr=0.25
#set your starting value for x here
start=400

#workarounds for the fact that we need a starting solution which will also be the old_solution by the end of the gradient descent
solution=start
old_solution=solution
i=0
#we don't know how long it will take
while True:
    #takes the  derivative (the gradient of the tangent line at the x point solution multiplied by the x point solution (the gradient of the function we are descending at that point)) and multiplies it by the learning rate
    gradient=derivative(solution)*lr
    #subtracts the gradient from solution to give a new x value
    solution=solution-gradient
    #for debug/coolness
    print(gradient)
    #ca=lcuates y by putting x into the function
    y=function(solution)
    #finds the c value for the x vale solution and the gradient gradient
    #commented out at it isn't needed for the graident descent but might be usefull to someone
    #c=calc_tangent(solution,gradient)
    #prints the x and y values that are our current best geusses
    print(solution,y)
    #if this x value is the same as the previous one
    if old_solution==solution:
        #break out of the loop
        break
    #this solution is now the old one as were about to update it 
    old_solution=solution
    #so it doesn't all happen instantly
    sleep(0.1)
    i+=1
