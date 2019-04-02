from time import sleep

#put your derivaitve from https://www.symbolab.com/solver/tangent-to-conic-calculator/derivative%20 here
def derivative(x):
    return 2*x+3
def calc_y(x,gradient):
    #rearnagement of y=mx+c to give c
    c=function(x)-gradient*x
    #does y=mx+c to find y
    return gradient*x+c
#put the fucntion you are decending here
def function(x):
    return x*x+3*x

#set your learning rate here
lr=0.25
#set your starting value for x here
start=4

#workarounds for the fact that we need a starting solution whihc will alos be the old_solution by the end of the graduent decent
solution=start
old_solution=solution

#we don't know how long it will take
while True:
    #takes the derovate (the gradient of the tangent line at the x point solution multiplied by the x point solution (the gradient of the function we are decending at that point)) and multpiles it by the learning rate
    gradient=derivative(solution)*lr
    #subtracts the gradient from solution to give a new x value
    solution=solution-gradient
    #for debug/coolness
    print(gradient)
    #finds the y value for the x vale solution and the gradient gradient
    y=calc_y(solution,gradient)
    
    #prints the x and y values that are our current geuss
    print(solution,y)
    #if this x value is the same as the previous one
    if old_solution==solution:
        #break out of the loop
        break
    #this soltuon is now the old one as were about to update it 
    old_solution=solution
    #so it doesn't all happen isntantly
    sleep(0.1)
