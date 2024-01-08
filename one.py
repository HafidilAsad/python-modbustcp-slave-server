#mengambil library modbus
import modbus_server 
from flask import Flask, request
import time

#menentukan port modbus
s = modbus_server.Server(port=503)



#menjalankan server
s.start()

app = Flask(__name__)

#membuat address 0 menjadi 1(true) 0 (false)

s.set_discrete_input(0, True)

# Endpoint untuk menerima permintaan POST dari web user
@app.route('/change_value', methods=['POST'])
def change_value():
    # Mendapatkan data dari permintaan POST
    req_data = request.get_json()
    
    # Jika terdapat payload dan aksi adalah 'false', set nilai input diskrit ke False
    if req_data and req_data.get('action') == 'false':
        return "Nilai telah diubah menjadi False"
    # Jika aksi adalah 'true', set nilai input diskrit ke True
    elif req_data and req_data.get('action') == 'true':
       
        return "Nilai telah diubah menjadi True"
    else:
        return "Permintaan tidak valid atau tidak ada perubahan nilai"
    

# menjalankan flask
if __name__ == '__main__':
    app.run(debug=True, port=5100)  




#untuk timing
# while True:
#     # Mengatur nilai input diskrit ke False
#     s.set_discrete_input(0, False)
    
#     # Menunggu 1 detik
#     time.sleep(1)
    
#     # Mengatur nilai input diskrit ke True setelah 1 detik
#     s.set_discrete_input(0, True)
    
#     # Menunggu 1 detik lagi
#     time.sleep(1)
