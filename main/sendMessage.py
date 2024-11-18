
# importing the module
import pywhatkit
 
# using Exception Handling to avoid 
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg_instantly("+6281280862017", 
                        "Test Untuk auto Send Message", 10, tab_close=True)
  print("Successfully Sent!")
 
except:
   
  # handling exception 
  # and printing error message
  print("An Unexpected Error!")