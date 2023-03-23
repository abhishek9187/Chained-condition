# wap to find smallest number in given list
smallest= None
for i in [31,41,55,12,9,15]:
    if smallest is None or i < smallest:
        smallest = i
        
print ('smallest  : ',smallest)
