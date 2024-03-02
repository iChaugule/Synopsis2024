import speech_recognition
import pyttsx3
import time
import paho.mqtt.publish as publish

recognizer = speech_recognition.Recognizer()
recognizer.energy_threshold = 800
recognizer.pause_threshold = 0.1
recognizer.phrase_threshold = 0.2
recognizer.non_speaking_duration = 0.1
recognizer.dynamic_energy_threshold = False

print("The Value is:" + str(recognizer.pause_threshold))
print("The Energy is:" + str(recognizer.energy_threshold))
print("The Non Speaking is:" + str(recognizer.non_speaking_duration))
print("The Phrase is:" + str(recognizer.phrase_threshold))

while True:

  try:

    with speech_recognition.Microphone() as mic:

      recognizer.adjust_for_ambient_noise(mic, duration=0.2)

      print("Say Command.....................................")
      audio = recognizer.listen(mic, timeout=3)
      #print("Stop listening")

      text = recognizer.recognize_google(audio, language='en-US', )
      #print(f"Recieved From Dictionary {text}")
      text = text.lower()
      print(f"Recognized{text}")

      publish.single("semi/commands", text, hostname="test.mosquitto.org")


  except speech_recognition.UnknownValueError:

    print("Could not understand audio")
    #recognizer = speech_recognition.Recognizer()
    continue
  
  except speech_recognition.RequestError as e:  
   
    print("Recog Error; {0}".format(e))
    #recognizer = speech_recognition.Recognizer()
    continue           
  

  except speech_recognition.WaitTimeoutError:  
   
    print("Wait timeout")
    #recognizer = speech_recognition.Recognizer()
    continue
