try:
    #Do something
    #value = 2
    print(value)
    #a = 1/0
    #print(a)
except (ZeroDivisionError, NameError) as e:
    #Handle the error
    print("No puedes dividir entre cero", e)
#except NameError:
#    print("Variable no definida")
#except:
#    print("Cualquier error")
else:
    #Only if no exception is raised
    print("No hubo excepciones")
finally:
    #Cleanup
    print("Siempre se ejecuta")


#b = 1 / 0
print(b)
