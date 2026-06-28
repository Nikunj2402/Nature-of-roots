# Nature of roots of quadratic equation

import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init() 
    engine.setProperty('rate', 185)   # Speed (default ~200)
    engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)
    voices = engine.getProperty('voices')    
    engine.setProperty('voice', voices[0].id)  # initialize every time
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.3)

print("WELCOME TO MATHBOT📐")
print("YOU CAN CHECK THE NATURE OF ROOTS OF A QUADRATIC EQUATION OF THE FORM ax² + bx + c = 0 HERE!")
speak("Hello!, I am a math bot. I can tell you about the nature of roots of a quadratic equation!")
print("Please enter the values of a, b and c")
speak("Please enter the values of A B and C one by one")

a=int(input("a = "))
if a<0:
    speak("A is minus"+ str(a))
else:
    speak("A is"+ str(a))

b=int(input("b = "))
if b<0:
    speak("B is minus"+ str(b))
else:
    speak("B is"+ str(b))

c=int(input("c = "))
if c<0:
    speak("C is minus"+ str(c))
else:
    speak("C is"+ str(c))

if a==0 and b==0:
    print("Invalid values")
    speak("You have entered wrong values, quadratic equation is not possible with these values! thank you")
    exit()

if a>0 and b>0 and c>0:
    print("Your equation is",a,"x² + ",b,"x + ",c," = 0")
elif a>0 and b>0 and c<0:
    print("Your equation is",a,"x² + ",b,"x - ",abs(c)," = 0")
elif a>0 and b<0 and c>0:
    print("Your equation is",a,"x² - ",abs(b),"x + ",c," = 0")
elif a>0 and b<0 and c<0:
    print("Your equation is",a,"x² - ",abs(b),"x - ",abs(c)," = 0")
elif a==0:
    print("Your equation is",b,"x + ",c," = 0")
elif b==0:
    print("Your equation is",a,"x² + ",c," = 0")
elif c==0:
    print("Your equation is",a,"x² + ",b,"x"" = 0")

speak("Ok I have your eqution now, I am working on it")
if (b**2 + 4*(a)*(c))>0:
    print("Real Roots")
    speak("your equation has real roots! THANK YOU!")
elif (b**2 + 4*(a)*(c))<0:
    print("Imaginary Roots")
    speak("your equation has imaginary roots! THANK YOU!")
else:
    print("Real and Equal Roots")
    speak("your equation has real and equal roots! THANK YOU!")