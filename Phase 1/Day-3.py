def Process_Batch(Input_List, Weights, Bais):
    
    results = []
    
    for Inputs in Input_List:
        
        Total_Signal = sum(i * w for i , w in zip(Inputs, Weights)) + Bais
        
        Output = 1 if Total_Signal >= 0 else 0
        
        results.append(Output)
        
    return results

Data = [[1,1], [1,0], [0,1], [0,0]]
Current_Weights = [0.5, 0.5]
Current_Bias = - 0.7

print(f"Batch Processing Results: {Process_Batch(Data, Current_Weights, Current_Bias)}")