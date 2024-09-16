#TempConvert.py
#Name: Colby Salak 
#Date: 9/15/20224
#Assignment: TempConvert.psy


def main():
  #Prompt the user for a Fahrenheit temperature
  print("State a temperature in degrees Fahrenheit and I will convert it into degrees Celsius")
  answer = input("Temperature in degrees Fahrenheit")
  Ftemp = float(answer)
  
  #Convert that temperature to celsius, rounding to 1 decimal percision
  Ctemp = (Ftemp - 32)/1.8
  Ctemp = round(Ctemp, 1)
  
  #Output converted temperature.
  Ctemp = str(Ctemp)
  Ftemp = str(Ftemp)
  print(Ftemp = "degrees Fahrenheit is" +Ctemp + "degrees Celsius"
  
if __name__ == '__main__':
  main()
