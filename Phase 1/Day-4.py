import time
 
def Slow_Processing(Data):
    
    Satrt_Time = time.time()
    
    Resutls = []
    
    for x in Data:
        
        time.sleep(0.01)
        
        Resutls.append(x * 2)
        
    End_Time = time.time()
    
    return End_Time - Satrt_Time

Data_List = list(range(100))

print(f"Time taken (Sequential): {Slow_Processing(Data_List):.4f} seconds")
