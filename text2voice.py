
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 

import sys

#module for playing the mp3 file
import playsound
  
# This module is imported so that we can play the converted audio 
import os  
# The text that you want to convert to audio

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class nottxt(Error):
   """Raised when the input file is not PDF"""
   pass

def voiceconvert(file_name):
    
    try:
        
        mp3_name=" "
    
        if file_name.endswith('.txt'):
        
            mp3_name = file_name[:-4]
            
        else:
            
            raise nottxt
    
        mytext=""

        with open(file_name,"r") as file:
    
            for line in file:
        
                mytext=mytext + line
            
        file.close()
        
        speech=gTTS(mytext,'en',slow=False)

        mp3_name=mp3_name+".mp3"
    
        speech.save(mp3_name)
        
        x=input("Do you want to play the text file (y/n)\t")
    
        if( x == 'Y' or x == 'y'):
            
            playsound.playsound(mp3_name, True)
        
            print("\n\n------Done reading the content-----")
        
        return
        
    except IOError as e:
   
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))

        print("Hence cannot open the file")
        
    except nottxt:
 
        print("This input file is not TEXT file")
        
        return

    except: #handle other exceptions such as attribute errors
   
        print ("Unexpected error:", sys.exc_info()[0])
    
