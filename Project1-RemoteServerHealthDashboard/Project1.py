import functions
import paramiko
target=[
    {"hostname": "192.168.206.130" , "port":22,"username": "root","password": "123"},
    {"hostname": "192.168.206.130" , "port":22,"username": "Hakem","password": "123"}
]
cmd="ls -la "
for host in target:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Paramiko checks the server’s host key to verify its identity, 
        # so we set the policy to automatically add the host key if it's missing.
        #without this line, the connection would fail if the host key is not already known.

        client.connect(hostname=host["hostname"], port=host["port"], username=host["username"], password=host["password"])
        stdin, stdout, stderr = client.exec_command(cmd)
        print(f"Output from {host['username']}@{host['hostname']}:\n")
        functions.save_as_json(stdout.read().decode(), "remote-data.json")
        print(stdout.read().decode())
        
    except Exception as e:
        print(f"Failed to connect to {host['hostname']} as {host['username']}: {e}")
    finally:
        client.close()


