import RGB

myFirstLED=RGB.LED(0,222,255)
mySecondLED=RGB.LED(200,200,200)
myFirstLED.resetAll()
print(myFirstLED.getAll())
myFirstLED.maxAll()
print(myFirstLED.getAll())

