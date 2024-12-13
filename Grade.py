project= float(input("project score: "))
internal= float(input("internal score: "))
external= float(input("external score: "))
if(project>=50 and internal >=50 and external >= 50):
  total= project*(70/100)+ internal*(10/100) + external*(20/100)
  print(f'total:{total}')
  if(total > 90):
   print("A grade")
  elif(total>80 and total<=90):
   print("B grade")
  else:
   print("C grade")
if(external<50):
    print(f"failed in external{external}")
if(internal<50):
    print(f"failed in internal{internal}")
if(project<50):
    print(f"failed in project{project}")