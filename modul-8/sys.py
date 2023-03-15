import subprocess

domain = input('Wprowadź adres do sprawdzenia: ')
output = subprocess.run(['ping', '-c', '1', domain], shell=True, capture_output=True)
print(output.stdout.decode('utf8'))