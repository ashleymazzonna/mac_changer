import subprocess   # allows us to use system commands
import optparse

interface = input("interface > ")
new_mac = input("new MAC > ")

parser = optparse.OptionParser() # creates an instance of the optparse object
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")   # adds options to the objects
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")   # adds options to the objects

parser.parse_args()

print("[+] Interface to change: " + interface + " -- New MAC: " + new_mac)


# will stop the user from being able to hijack the flow of
# the program (will not be able to execute multiple commands using a comma)
subprocess.call((["ifconfig", interface, "down"]))
subprocess.call((["ifconfig", interface, "hw", "ether", new_mac]))
subprocess.call((["ifconfig", interface, "up"]))




