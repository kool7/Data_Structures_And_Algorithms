weight = 0.1
def neural_network(input, weight):
    prediction = input * weight
    return prediction 

input = 8.5
pred = neural_network(input, weight)
print(pred)