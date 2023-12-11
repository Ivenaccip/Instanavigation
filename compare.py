import subprocess

def ejecutar_comando(comando, use_sudo=False):
    """ Ejecuta un comando opcionalmente con sudo. """
    if use_sudo:
        comando = f"sudo {comando}"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proceso.communicate()
    return stdout.decode().strip(), stderr.decode().strip()

# Comando para ejecutar ChromeDriver
comando_chromedriver = "chromedriver --version"

# Ejecutar como usuario normal
stdout_user, stderr_user = ejecutar_comando(comando_chromedriver)
print("Resultado como usuario normal:")
print("stdout:", stdout_user)
print("stderr:", stderr_user)

# Ejecutar como root
stdout_root, stderr_root = ejecutar_comando(comando_chromedriver, use_sudo=True)
print("\nResultado como root:")
print("stdout:", stdout_root)
print("stderr:", stderr_root)

# Comparar resultados
if stdout_user == stdout_root and stderr_user == stderr_root:
    print("\nNo hay diferencias en la ejecución de ChromeDriver.")
else:
    print("\nHay diferencias en la ejecución de ChromeDriver.")
