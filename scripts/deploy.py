import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

# Construir imagen Docker
def build_docker_image():
    print("Building Docker image...")
    run_command("docker build -t my-app:latest ./app")

# Desplegar con Helm
def deploy_with_helm():
    print("Deploying application with Helm...")
    run_command("helm upgrade --install my-app ./helm-chart")

# Verificar estado del despliegue
def check_status():
    print("Verifying status...")
    run_command("kubectl get pods")

if __name__ == "__main__":
    build_docker_image()
    deploy_with_helm()
    check_status()
