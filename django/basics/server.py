from socket import *

def createServer():
  serverSocket = socket(AF_INET,SOCK_STREAM)
  try:
    serverSocket.bind(('localhost',9000))
    serverSocket.listen(5)
    while(1):
      (clientsocket,address) = serverSocket.accept()
      rd = clientsocket.recv(5000).decode()
      pieces = rd.split("\n")
      if( len(pieces) > 0) : print(pieces[0])
      
      
      data = "HTTP/1.1 200 OR\r\n"
      data += "Content-Type: text/html; charset=utf-8\r\n"
      data += "\r\n"
      data += "<html><body>Hello world</body></html>\r\n\r\n"
      clientsocket.sendall(data.encode())
      clientsocket.shutdown(SHUT_WR)
  except KeyboardInterrupt:
    print("\nShutting down...\n")
  except Exception as exc:
    print("Error:\n")
    print(exc)
    
  serverSocket.close()
  
print("Access http://localhost:9000")
createServer()