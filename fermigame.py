# Python
import random
def unique(og):
   return len(set(str(og))) == len(str(og))
   
print('enter a number of digit:')
n=int(input())
if n==2 :
   ogg=[num for num in range(10,100) if  unique(num)]
   original_number=str(random.choice(ogg))
elif n==3:
   ogg=[num for num in range(100,1000) if  unique(num)]
   original_number=str(random.choice(ogg))
else:
   ogg=[num for num in range(1000,10000) if  unique(num)]
   original_number=str(random.choice(ogg))
   
## create infinite while loop
while True:
## step 2 and step 6
   guess_number=str(input('guess the number....'))
   output=[]
## step 3 and step 4 (use continue statement)
   while(len(original_number) != len(guess_number)):
    guess_number=str(input('enter ' + str(len(original_number)) + ' digits number'))
    break
   if(len(guess_number) != len(set(guess_number))):
    print('duplicate number')
    continue;
## step 5 (use break statement for winning condition)
   if((int(original_number)-int(guess_number)) == 0):
      print("Fermi   "* len(original_number))
      print('YOU Won......')
      break;
      
      
## step 7
   for j in range(len(original_number)):
        for k in range(len(guess_number)):
            if(j==k):
                if(original_number[j] == guess_number[k]):
                    output.append('Fermi')
            else:
                if(original_number[j] == guess_number[k]):
                    output.append('Pico')
## step 8
   output_string=''
   for l in output:
      output_string = output_string + '   ' + l
      

## step 9
   if(len(output)== 0):
    print('Bagel')
   else:
    print(output_string)
