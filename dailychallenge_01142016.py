from base64 import b64encode, b64decode
speech = 'And Crispian shall never go by From this day to the ending of the world But we in it shall be remembered  We few we happy few we band of brothers'
print ' '.join(['\n{}'.format(x) if x[0].isupper() and x not in ['And','Crispian'] else x for x in speech.split() ])


mystring = "speech = 'And Crispian shall never go by From this day to the ending of the world But we in it shall be remembered  We few we happy few we band of brothers'\n"
mystring += "print ' '.join(['\\n{}'.format(x) if x[0].isupper() and x not in ['And','Crispian'] else x for x in speech.split() ])"


#mystring = "print ' '.join(['\\n{}'.format(x) if x[0].isupper() and x not in ['And','Crispian'] else x for x in speech.split() ])"
print b64encode(mystring)
print b64decode(b64encode(mystring))