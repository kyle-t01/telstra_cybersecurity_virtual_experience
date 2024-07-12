# www.theforage.com - Telstra Cyber Task 3
# Firewall Server Handler


from http.server import BaseHTTPRequestHandler, HTTPServer


host = "localhost"
port = 8000


#########

malicious_header = {
    "suffix": "%>//",
    "c1": "Runtime",
    "c2": "<%",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded",
}

denied_path = "/tomcatwar.jsp"


# Handle the response here 
def block_request(self):
    print("Blocking request")


def handle_request(self):
    # compare request path
    if self.path == denied_path:
        for malicious_key in malicious_header.keys():
            if malicious_key in self.headers:
                if self.headers[malicious_key] == malicious_header[malicious_key]:
                    return block_request(self)
    

    self.send_response(200)
    self.send_header("content-type", "application/json")
    self.end_headers()


#########




class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handle_request(self)


    def do_POST(self):
        handle_request(self)


if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))


    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)