from process_monitor import monitor_process
#from switch_status import get_sss
import thread


def main():
    try:
        print ("statring")
        thread.start_new_thread( monitor_process, ( "process_monitor",) )
        thread.start_new_thread( get_sss, ("sss_status", ) )
    except:
        print "Error: unable to start thread"

    while True:
       pass



if __name__=="__main__":
    main()
