def Process_Batch(Input_List, Weights, Bais):
    
    results = []
    
    for Inputs in Input_List:
        
        Total_Signal = sum(i * w for i , w in zip(Inputs, Weights)) + Bais
        
        Output = 1 if Total_Signal >= 0 else 0
        
        results.append(Output)
        
    return results

Data = []

Current_Weights = []

Current_Bais = []

print(f"Batch Processing Results: {process_batch(data, current_weights, current_bias)}")