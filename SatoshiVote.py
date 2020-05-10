#SatoshiVote By Harry Robson
from bitcoin import *
import qrcode
import os

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


    

#Generate bitcoin keys and addresses
def create_keys(num_address):
    h = (num_address)
    w = 3
    address_matrix = [[0 for x in range(w)] for y in range(h)]
    
    for_counter = 0
    for i in range(0, num_address):
        priv_key = random_key()
        pub_key = privtopub(priv_key)
        address = pubtoaddr(pub_key)
        address_matrix[(for_counter)][0] = (priv_key)
        address_matrix[(for_counter)][1] = (address)
        address_matrix[(for_counter)][2] = (for_counter)
        for_counter = for_counter + 1
    return address_matrix

#Generate QR code for each address
def create_qr_codes(address_matrix, num_address, desktop_path):
    for_counter = 0
    for i in range(0, num_address):
        img = qrcode.make(address_matrix[(for_counter)][1])
        img.save((desktop_path) + "\satoshivote" + str((for_counter + 1)) + ".png")
        for_counter = for_counter + 1

#Monitor results
def monitor_results(address_matrix, num_address):
    while True:
        for_counter = 0
        time.sleep(5)
        print("\n")
        for i in range(0, num_address):
            txs = history(address_matrix[(for_counter)][1])
            tx_count = len(txs)
            print("Option " + (str(for_counter + 1)) + ": " + str((tx_count))) 
            for_counter = for_counter + 1

while True:
    mode = input("Start new campaign (1) or monitor an ongoing campign (2)? ")
    if mode == "1":
        num_address = int(input("How many options are there? "))
        address_matrix = create_keys(num_address)
        create_qr_codes(address_matrix, num_address, desktop_path)
        view_results = input("Do you want to view the live results? y/n ")
        if view_results == "y":
            monitor_results(address_matrix, num_address)
        else:
            print("test")
    elif mode == "2":
        print("Create a .txt document containing an address on each line that you would like to monitor")
        file_location = input("enter the path of the file")
        address_list = []
        f = open((file_location), "r")
        for line in f:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            address_list.append(line_list)
        f.close()
        while Trie:
            for_counter = 0
            time.sleep(5)
            print("\n")
            for i in range(0, len(address_list)):
                txs = history(address_list[for_counter])
                tx_count = len(txs)
                print("Option " + (str(for_counter + 1)) + ": " + str((tx_count)))
                for_counter = for_counter + 1
                
        
