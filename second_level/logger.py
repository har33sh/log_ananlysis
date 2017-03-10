from process_monitor import monitor_process
#from switch_status import get_sss
import thread
import json
import socket



def get_ip(): #function returns the ip address of the machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("internet.iitb.ac.in",80))
    ip= (s.getsockname()[0])
    s.close()
    return ip



def main():
    try:
        print ("statring")
        thread.start_new_thread( monitor_process, ( "process_monitor",) )
        if machine_type=="rpi":
            thread.start_new_thread( get_sss, ("sss_status", ) )
    except:
        print "Error: unable to start thread"

    while True:
       pass



if __name__=="__main__":
    conf = json.load(open('config.json'))
    machine_type= conf[get_ip()] ["type"]
    main()
