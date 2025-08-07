try:
    file=open('output.txt','r')
    print('Line1:',file.readline())
    print('Line2:',file.readline())
    file.close()
except:
    print("ERROR: The file 'output.txt' was not found.")
