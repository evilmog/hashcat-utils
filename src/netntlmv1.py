# This is a script to convert NetNTLMv1 hashes into a format
# crackable by hashcat -m 14000 to allow conversion to ntlm.
# atom thought of the idea https://hashcat.net/forum/thread-5832.html

import platform
import subprocess
import os

hash_input = raw_input("Please enter hash: ")

if not hash_input:
        hash_input="johndoe::test-domain:1FA1B9C4ED8E570200000000000000000000000000000000:1B91B89CC1A7417DF9CFAC47CCDED2B77D01513435B36DCA:1122334455667788"

h_user, h_blank, h_domain, h_hash1, h_hash2, h_challenge = hash_input.split(':')
h_split = h_hash2[32:48]
h_input1 = h_hash2[0:16]
h_input2 = h_hash2[16:32]

if platform.system() == 'Windows':
        print "echo '" + h_input1 + ":" + h_challenge + "' > " + h_user + ".hash"
        print "echo '" + h_input2 + ":" + h_challenge + "' >> " + h_user + ".hash"

if platform.system() == 'Linux':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        h_exec = dir_path + "/ct3_to_ntlm.bin"
        print "echo '" + h_input1 + ":" + h_challenge + "' > " + h_user + ".hash"
        print "echo '" + h_input2 + ":" + h_challenge + "' >> " + h_user + ".hash"
        p = subprocess.call([h_exec, h_split, h_challenge, h_hash1])
