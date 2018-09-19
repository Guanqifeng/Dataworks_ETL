from twisted.internet import protocol, reactor
from time import ctime

PORT = 11111

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        client = self.transport.getPeer().host
        print('....Connectioned from '+str(client))
    def dataReceived(self,data):
        self.transport.write(bytes("["+ctime()+"]:"+str(data),encoding='utf-8'))
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('Waiting for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()






