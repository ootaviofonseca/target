def fibonacci(entrada):
    if entrada == 0 or entrada == 1:
        return True
    else:
        sequenciaFib = [0, 1] 
        
        
        while sequenciaFib[-1] < entrada:
            sequenciaFib.append(sequenciaFib[-1] + sequenciaFib[-2])
      
        if entrada in sequenciaFib: 
            return True 
        else:
            return False

entrada = int(input())
if entrada >= 0 :
    if fibonacci(entrada): 
        print(f"O número {entrada} está na sequência")
    else: 
        print(f"O número {entrada} não está na sequência")