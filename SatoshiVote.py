#SatoshiVote by Harry Robson
from bitcoin import *
import qrcode
import os

#Generate Bitcoin keys
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

#Generate QR code for each address and output address details
def create_qr_codes(address_matrix, num_address, desktop_path):
    for_counter = 0
    for i in range(0, num_address):
        img = qrcode.make(address_matrix[(for_counter)][1])
        img.save((desktop_path) + "\satoshivote" + str((for_counter + 1)) + ".png")
        for_counter = for_counter + 1
    #Save addresses to one file, private keys to another
    f = open((desktop_path) + "\\address_list.txt","w+")
    for_counter = 0
    for i in range(0, num_address):
        f.write(str(address_matrix[int(for_counter)][1]) + "\n")
        for_counter = for_counter + 1
    f.close()
    f = open((desktop_path) + "\\private_list.txt", "w+")
    for_counter = 0
    for i in range(0, num_address):
        f.write(str(address_matrix[int(for_counter)][0]) + "\n")
        for_counter = for_counter + 1
        
#View live results
def monitor_results(address_matrix, num_address, address_list):
    while True:
        for_counter = 0
        time.sleep(5)
        print("\n")
        for i in range(0, num_address):
            txs = history(address_matrix[(for_counter)][1])
            tx_count = len(txs)
            print("Option " + (str(for_counter + 1)) + ": " + str((tx_count))) 
            for_counter = for_counter + 1

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

#Calling functions
while True:
    user_option = input("Start new campaign (1) or view results of a current campaign (2) ")
    if user_option == "1":
        num_address = int(input("How many candidates? "))
        address_matrix = create_keys(num_address)
        create_qr_codes(address_matrix, num_address, desktop_path)
    if user_option == "2":
        num_address = int(input("How many candidates? "))
        print("Gathering results...")
        address_matrix = create_keys(num_address)
        #Need to open address file and read off one by one.
        address_list = []
        f = open((desktop_path + "\\address_list.txt"), "r")
        for line in f:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            address_list.append(line_list)
        f.close()
        monitor_results(address_matrix, num_address, address_list)
