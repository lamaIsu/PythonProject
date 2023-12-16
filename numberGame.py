import random
class invalidInput (Exception):
  "the input should be 4 integer"
  pass
  

print("You have to guess number of 4 digit to find the correct number\nYou have 10 chance")
def corrPlace(userNum,correctNum):
  corrCount=0
  for i in range(0,4):
    if userNum[i]==correctNum[i]:
      corrCount+=1
    i+=1
  return corrCount
def containDigit(userNum,correctNum):
  countFind=0
  str(correctNum)
  for i in range(0,4):
    if correctNum.find(userNum[i])!=-1:
      countFind+=1
  return countFind
def findError(userNum):
  if len(userNum)!=4:
    raise invalidInput
      
try:
  correctNum=str( random.randrange(1000,10000))
  count=1
  for i in range(0,5):
    
    print("chance number ",count)
    userNum= input("enter your number: ")
    findError(userNum)
    if corrPlace(userNum,correctNum) ==4:
      print("You find it !")
      break
    print("There is ",corrPlace(userNum,correctNum)," number in the same place")
    print("There is ",(containDigit(userNum,correctNum)-corrPlace(userNum,correctNum))," number correct but not in the same place")
    count+=1
  print("The correct number is: ",correctNum," Try again :(")
except invalidInput as e:
  print("the input should be 4 integer")
  


  



  
  