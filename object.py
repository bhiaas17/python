#!/usr/bin/env python2 
''' The Program is related to the basic data type of python and also define the object.Every object has an identity, a type and a value."raw_input" store the string value'''
print "Object features:"
print "\t\t 1.Object identity"
print "\t\t 2.Object data type"
print "\t\t 3.Object value "

				#python create the object and store in variable "a".
a=raw_input("Enter the object value :" )
				#object identity
print "object id: ",id(a) 
				#object class type
print "object data type:",type(a)
				#object value
print "object value: ",a
