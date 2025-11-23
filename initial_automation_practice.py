import ipaddress
import requests

# Authenticate with the IPstack library
api_key = 'INSERT HERE'

def authentication(key):
    result = requests.post('https://api.ipstack.com/', data=key)
    print(result)
    return result

ip_address = ipaddress.ip_address('192.168.1.1')
print(ip_address)

def standard_lookup():
    url = "https://api.ipstack.com/192.168.1.1"
    querystring = {"access_key":"57d694bd0b4b7c6d8398dad238d3d9ad"}
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    return response

authentication(api_key)
standard_lookup()

# Do a standard lookup of an IPv4 address

# What is a set
switches_set = {"switch3", "switch5", "switch1", "switch500", "switch2"}

# What is a list
acl_list = ["aclrule1", "aclrule2", "aclrule3", "aclrule4"]

# What is a dictionary
username_to_IP_dictionary = {"catniss":"192.178.50.1", "bobby":"192.178.50.2"}

ipaddress_adding = ipaddress.ip_address('192.168.1.1') + 10
print (ipaddress_adding)

ip_address_as_string = "192.168.1.1"
print(ip_address_as_string)

#ip_address_as_string_with_addition = "192.168.1.1" + 10 
#print(ip_address_as_string_with_addition)

switches_set.add("switch5000")
print(switches_set)

switch1_days_uptime = 65.4

switch2_days_uptime = 13.3

# Finds sum of days uptime for 2 switches
def add_days_uptime(uptime1, uptime2):
    result = uptime1 + uptime2
    print(result)
    return result

add_days_uptime(uptime1=switch1_days_uptime,uptime2=switch2_days_uptime)

firewall_active = True

# While firewall is active, show IPS events
#def show_ips_events():
#    while firewall_active == True:
#        print("Here are the IPS events")

#show_ips_events()

link_up = False

# Checks if primary link is up; if not, switch to ISP2
def reroute_traffic(link):
    if link == False:
        print("Traffic is now rerouted to ISP2")
    else: 
        pass
    return link
print("We love to code hahahaha")
print(link_up)
print(65)
print(64.78)
print(reroute_traffic(link_up))

reroute_traffic(link_up)