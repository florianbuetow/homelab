import paramiko


class ConnectionManager:

    def __init__(self):
        self.ssh_client = None

    def open_connection(self, host, username, password):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(host, username=username, password=password)
        print("SSH connection established")

    def close_connection(self):
        if self.ssh_client:
            self.ssh_client.close()
            self.ssh_client = None
            print("SSH connection closed")

    def execute(self, cmd):
        if not self.ssh_client:
            raise Exception("Connection not established. Please open connection first.")
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
        output = stdout.read().decode()
        error = stderr.read().decode()
        return output, error
