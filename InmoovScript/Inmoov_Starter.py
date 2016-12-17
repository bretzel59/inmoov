# ##############################################################################
# 								INMOOV SCRIPT
# This is base Inmoov script file ( fingerstarter )
# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a finger starter
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
# The Finger Starter is considered here to be right index, 
# so make sure your servo is connected to pin3 of you Arduino
# ##############################################################################



# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")


##############
# basic services declaration
i01 = Runtime.createAndStart("i01", "InMoov")
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech") #mouth = Runtime.createAndStart("i01.mouth", "NaturalReaderSpeach")

##############
# config files
#this is usefull about vocal startup commands diagnostic "starting mouth etc..."
mouth.setVoice("cmu-slt-hsmm") # TODO > remove and use default mouth
execfile('InmoovScript/Inmoov_Starter.ini') #TODO > import ConfigParser

##############
#starting parts
i01.startEar()
i01.startMouth()

##############
# robot checkup
execfile('InmoovScript/system/InitCheckup.py')

##############
# verbal commands

ear.addCommand("attach your finger", "i01.rightHand.index", "attach")
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open your finger", "python", "fingeropen")
ear.addCommand("close your finger", "python", "fingerclose")
ear.addCommand("finger to the middle", "python", "fingermiddle")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

#Arduino is ok ? lets go !
if RightPortIsConnected:
	i01.startRightHand(MyRightPort)


#The "u" is usefull to read UTF8 in other languages
def fingeropen():
  i01.moveHand("right",0,0,0,0,0)
  i01.mouth.speak(u"ok I open my finger")

def fingerclose():
  i01.moveHand("right",180,180,180,180,180)
  i01.mouth.speak(u"my finger is closed")

def fingermiddle():
  i01.moveHand("right",90,90,90,90,90)
  i01.mouth.speak(u"ok you have my attention")

  