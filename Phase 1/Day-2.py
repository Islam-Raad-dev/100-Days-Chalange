def And_Gate(Input1, Input2):
    
    Wight1 = 0.5
    Wight2 = 0.5
    bias = -0.7
    
    Total_Signal = (Input1 * Wight1) + ( Input2 * Wight2) + bias
    
    if Total_Signal >= 0:
        
            return 1
    else:
            return 0
        

print("Input (1, 1) -> Output:")
print(And_Gate(1, 1))
print("Input (1, 0) -> Output:" )
print(And_Gate(1, 0))

def Or_Gate(Input1, Input2):
    
    Wight1 = 0.3
    Wight2 = 0.3
    bias = -0.1
    
    Total_Signal = (Input1 * Wight1) + ( Input2 * Wight2) + bias
    
    if Total_Signal >= 0:
        
            return 1
    else:
            return 0
        
print("------------OR Gate-------------")
print("Input (1, 1) -> Output:")
print(Or_Gate(1, 1))
print("Input (1, 0) -> Output:" )
print(Or_Gate(1, 0))
print("Input (1, 1) -> Output:")
print(Or_Gate(0, 0))