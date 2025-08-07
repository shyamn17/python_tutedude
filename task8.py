a=input("Enter text to write a file:")
file=open('output.txt','a')
file.write(a + '\n')
print('Data successfully written to output.txt')
file.close()


b=input("Enter additional text to append:")
file=open('output.txt','a')
file.writelines(b)
print('Data successfully appended')
file.close()

file=open('output.txt','r')
print('Final content of output.txt:')
print(file.read())
file.close()
