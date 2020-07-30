from N4Tools import terminal
import threading as t

class intro:
   def __init__(self):
      T = t.Thread(target=self.handler)
      T.start()

   def handler(self):
      width = terminal().size['width'] # 100
      while True:
         if width != terminal().size['width']: # ?
            width = terminal().size['width']
            self.on_width(width)

   def on_width(self,width):
      print(width)

intro()
