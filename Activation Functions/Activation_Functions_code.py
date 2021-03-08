import math
print("Enter the number of input signals")
n = int(input())
print("Enter the input signal values")
input_signal = list(map(int,input().split()))[:n]
print("Enter the weights for each signal to be multiplied")
weights = list(map(int,input().split()))[:n]
print("Enter the bias value of the neuron")
bias = float(input())
output = 0
weighted_sum_of_input=[]
for i,j in zip(input_signal,weights):
    weighted_sum_of_input.append(i*j)

input_to_activation_function = sum(weighted_sum_of_input) + bias
print("The input to activation funtion is :")
print(input_to_activation_function)

print("Choose an activation fuction to apply :")
print("1. Linear Function")
print("2. Sigmoid Function")
print("3. TanH Function")
print("4. ReLU Function")
print("5. Leaky ReLU Function")
print("6. Parametric Function")
print("7. Softplus Function")
print("8. Exponential Linear Unit Function")
print("9. Binary Step Function")
print("10. ArcTan Function")
print("11. Gaussian Function")
print("12. Swish Function")
print("13. Bipolar Function")
print("14. Output Applying All Functions")

choice = int(input())
if(choice == 1):
    out = input_to_activation_function
    print("Output after applying Linear Transformation is: ", out)
elif(choice == 2):
    out = 1/(1 + math.exp(-input_to_activation_function))
    print("Output after applying Sigmoid Function is: ", out)
elif(choice == 3):
    out = (2/(1 + math.exp(-2*input_to_activation_function)))-1
    print("Output after applying TanH Function is: ", out)
elif(choice == 4):
    out = max(0,input_to_activation_function)
    print("Output after applying ReLU Function is: ", out)
elif(choice == 5):
    if(input_to_activation_function < 0):
        out = 0.01*input_to_activation_function
    else:
        out = input_to_activation_function
    print("Output after applying Leaky ReLU Function is: ", out)
elif(choice == 6):
    print("Enter a value of alpha(Slope of neagtive part) as float")
    alpha=float(input())
    if(input_to_activation_function < 0):
        out = alpha*input_to_activation_function
    else:
        out = input_to_activation_function
    print("Output after applying Parametric ReLU Function is: ", out)
elif(choice == 7):
    out = math.log(1 + math.exp(input_to_activation_function))
    print("Output after applying Softplus Function is: ", out)
elif(choice == 8):
    print("Enter a value of alpha as float")
    alpha=float(input())
    if(input_to_activation_function <= 0):
        out = (alpha*math.exp(input_to_activation_function))-1
    else:
        out = input_to_activation_function
    print("Output after applying Exponential Linear Unit Function is: ", out)
elif(choice == 9):
    if(input_to_activation_function < 0):
        out = 0
    else:
        out = 1
    print("Output after applying Binary Step Function is: ", out)
elif(choice == 10):
    out = math.atan(input_to_activation_function)
    print("Output after applying ArcTan Function is: ", out)
elif(choice == 11):
    print("Enter the mean in float")
    mean = float(input())
    print("Enter the Standard Deviation in float")
    sd = float(input())
    out = (1/(math.sqrt(2*math.pi*sd)))*math.exp(-((input_to_activation_function-mean)**2/(2*sd*sd)))
    print("Output after applying Gaussian Function is: ", out)
elif(choice == 12):
    out =  input_to_activation_function/(1+math.exp(-input_to_activation_function))
    print("Output after applying Swish Function is: ", out)
elif(choice == 13):
    if(input_to_activation_function < 0):
        out = -1
    else:
        out = 1
    print("Output after applying BiPolar Function is: ", out)
elif(choice == 14):
    out = input_to_activation_function
    print("Output after applying Linear Transformation is: ", out)
    out = 1/(1 + math.exp(-input_to_activation_function))
    print("Output after applying Sigmoid Function is: ", out)
    out = (2/(1 + math.exp(-2*input_to_activation_function)))-1
    print("Output after applying TanH Function is: ", out)
    out = max(0,input_to_activation_function)
    print("Output after applying ReLU Function is: ", out)
    if(input_to_activation_function < 0):
        out = 0.01*input_to_activation_function
    else:
        out = input_to_activation_function
    print("Output after applying Leaky ReLU Function is: ", out)
    print("Enter a value of alpha(Slope of neagtive part) as float")
    alpha=float(input())
    if(input_to_activation_function < 0):
        out = alpha*input_to_activation_function
    else:
        out = input_to_activation_function
    print("Output after applying Parametric ReLU Function is: ", out)
    out = math.log(1 + math.exp(input_to_activation_function))
    print("Output after applying Softplus Function is: ", out)
    print("Enter a value of alpha as float")
    alpha=float(input())
    if(input_to_activation_function <= 0):
        out = (alpha*math.exp(input_to_activation_function))-1
    else:
        out = input_to_activation_function
    print("Output after applying Parametric ReLU Function is: ", out)
    if(input_to_activation_function < 0):
        out = 0
    else:
        out = 1
    print("Output after applying Binary Step Function is: ", out)
    out = math.atan(input_to_activation_function)
    print("Output after applying ArcTan Function is: ", out)
    print("Enter the mean in float")
    mean = float(input())
    print("Enter the Standard Deviation in float")
    sd = float(input())
    out = (1/(math.sqrt(2*math.pi*sd)))*math.exp(-((input_to_activation_function-mean)**2/(2*sd*sd)))
    print("Output after applying Gaussian Function is: ", out)
    out =  input_to_activation_function/(1+math.exp(-input_to_activation_function))
    print("Output after applying Swish Function is: ", out)
    if(input_to_activation_function < 0):
        out = -1
    else:
        out = 1
    print("Output after applying BiPolar Function is: ", out)
