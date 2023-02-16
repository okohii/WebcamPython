# Você deve baixar no celular o aplicativo "IP Webcam" ou qualquer
# outro app que crie um ip para a câmera do celular, lembrando que
# o celular deve estar conectado a mesma rede WIFI que o host.


import requests
import cv2
import numpy as np
import imutils
  
# Nessa url, você vai colocar o ip que mostra no app.
url = "http://192.168.15.103:8080/shot.jpg"
  

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img)
  
    # Pressione a tecla "ESC" para sair
    if cv2.waitKey(1) == 27:
        break
  
cv2.destroyAllWindows()