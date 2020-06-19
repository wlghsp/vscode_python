x= [1,2,3]
y= [2,4,6]

def cost_func(W,x,y):
    s = 0
    for i in range(len(x)):
        s += (W * x[i] - y[i]) ** 2

    return s / len(x)

for feed_w in range(-5,6,1):
    curr_cost = cost_func(feed_w, x, y)
    print("{:6.3f} | {:10.5f}".format(feed_w, curr_cost))