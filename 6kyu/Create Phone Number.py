import numpy as np

def create_phone_number(n):
    n=np.array(n)
    if np.any(n>=10):
        return False 
    else:
        return f"({str(n[:3])[1:-1].replace(' ', '')}) {str(n[3:6])[1:-1].replace(' ', '')}-{str(n[6:])[1:-1].replace(' ','')}"

