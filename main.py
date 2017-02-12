import requests
import struct
import socket
import json
from xml.etree import ElementTree
from amfast.encoder import Encoder

xml_url = "http://196.evony.com/config.xml"
s = requests.Session()


def get_xml_data():
    """Get XML Data From evony"""

    r = s.get(xml_url)
    tree = ElementTree.fromstring(r.content)
    server = tree[5].text
    port = tree[6].text
    return server, port


def open_connection(server, port):

    username = "nab196@yahoo.com"
    password = "1neatpw!"

    udata = {'user': username, 'pwd': password}
    data = {'cmd': 'login', 'data': udata}

    enc = Encoder(amf3=True)
    obj = enc.encode(data)
    bytes_send = str(len(obj)) + obj

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, int(port)))
    sent = sock.send(bytes_send)
    print ("Send Data : ", bytes_send)
    data = sock.recv(1024)
    print("Received Data : ", data)


if __name__ == "__main__":
    server, port = get_xml_data()
    if server and port:
        print ("Server : ", server)
        print ("Port : ", port)
        open_connection(server, port)
    else:
        print("No Server And Port Found")
