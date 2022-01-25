myDict = {
    'py':'python',
    'cpp':'C++',
    'c':'C',
    'js':'JavaScript',
    'java':'Java'
    }
filename = input("Input the Filename: ")
extens = filename.split(".")
x = myDict[(extens[-1])]
print ("The extension of the file is :","'",x,"'")    


#NOTE: The above program is done w.r.t the question's sample output i.e.
#Input the Filename: abc.py The extension of the file is : 'python'
#Which means the sample output does not directly print the the extension
#but instead the language name
#So, I made a dictionary for a few extensions with their languages

#For a program to just print out the extension of the file name,
#Below is the code

filename = input("Input the Filename: ")
extens = filename.split(".")
print ("The extension of the file is :","'",(extens[-1]),"'")



    


        
   
    






