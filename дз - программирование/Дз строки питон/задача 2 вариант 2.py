n = int(input().strip())
    
target = str(n)
pos = 1
current = 1
    
while True:
    num_str = str(current)
    
    if target in num_str:
        idx = num_str.find(target)
        print(pos + idx)
         
        
    next_num = current + 1
    next_str = str(next_num)
       
    for overlap in range(1, len(target)):
        if overlap <= len(num_str) and len(target) - overlap <= len(next_str):
            if num_str[-overlap:] + next_str[:len(target)-overlap] == target:
                print(pos + len(num_str) - overlap)
    return
        
    pos += len(num_str)
    current += 1
