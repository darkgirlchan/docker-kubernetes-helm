# Project: Application Deployment with Docker, Kubernetes, and Helm

This project contains a sample application deployed using Docker, Kubernetes, and Helm. Below are the instructions for installation, execution, and maintenance of the project.

---

## **Prerequisites**

Before you begin, ensure that the following tools are installed on your system:

- **Docker** - For creating and managing containers.
- **Kubernetes** - For container orchestration.
- **Helm** - For managing Kubernetes deployments.
- **kubectl** - Kubernetes command-line tool.
- **Git** - For cloning the repository.

### **Install Docker**
- Follow the instructions on the [Docker Docs](https://docs.docker.com/get-docker/) to install Docker.

### **Install Kubernetes**
- If you are using Docker Desktop, Kubernetes is already installed.
- For other platforms, follow the [Kubernetes installation guide](https://kubernetes.io/docs/setup/).

### **Install Helm**
- Follow the instructions on [Helm Docs](https://helm.sh/docs/intro/install/) to install Helm.

---

## **Clone the repository**

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

---

## **Building the Docker Image**

1. Navigate to the directory containing your `Dockerfile` (e.g., `./app`).
2. Build the Docker image:

   ```bash
   docker build -t my-app:latest ./app
   ```

   This will create an image called `my-app` with the `latest` tag.

3. Verify that the image was created successfully:

   ```bash
   docker images
   ```

---

## **Deploy the Application on Kubernetes using Helm**

### **Preparing Helm**

1. Ensure the `values.yaml` file is correctly configured. This file defines parameters like the Docker image to use and other deployment configurations.
   
   **Example `values.yaml`:**

   ```yaml
   image:
     repository: my-app
     tag: latest
     pullPolicy: IfNotPresent
   ```

### **Install or Upgrade the Application with Helm**

To deploy or upgrade the application in Kubernetes, run the following:

```bash
helm upgrade --install my-app ./helm-chart
```

This command will install or upgrade the `my-app` application using the configured Helm chart.

### **Verify the Deployment**

After running the above command, you can verify that the application pods are running with:

```bash
kubectl get pods
```

If everything is correct, you should see your application pods in the `Running` state.

---

## **Expose the Application as a Service**

The application is configured to be accessible via a Kubernetes service. If you used the `service.yaml` file, the service will be available on a node port.

### **Verify the Service**

To check the service:

```bash
kubectl get svc
```

The service should appear with a port assigned, allowing you to access the application within the Kubernetes cluster.

---

## **Maintenance and Updates**

### **Update the Docker Image**

If you make changes to your application and need to update the Docker image:

1. **Rebuild the image:**

   ```bash
   docker build -t my-app:latest ./app
   ```

2. **Push the new image to Docker Hub (if using Docker Hub):**

   ```bash
   docker tag my-app:latest your-username/my-app:latest
   docker push your-username/my-app:latest
   ```

3. **Update the deployment in Kubernetes:**

   If using Helm:

   ```bash
   helm upgrade --install my-app ./helm-chart
   ```

   If using direct YAML manifests:

   ```bash
   kubectl apply -f kubernetes-manifests/deployment.yaml
   ```

### **Review Pod Logs**

If you need to review the logs of your application for debugging, you can use the following command:

```bash
kubectl logs <pod-name>
```

Replace `<pod-name>` with the name of the pod you want to check. You can get the pod names with:

```bash
kubectl get pods
```

---

## **Uninstalling the Application**

To uninstall the application from Kubernetes, you can run:

### **Using Helm**

```bash
helm uninstall my-app
```

### **Using YAML Manifests**

If you are not using Helm and only using YAML manifests, remove the resources with:

```bash
kubectl delete -f kubernetes-manifests/deployment.yaml
kubectl delete -f kubernetes-manifests/service.yaml
```

---

## **Common Issues**

1. **Error: `ImagePullBackOff`**
   - Ensure the image is available in Docker or your image repository.
   - If the image is in a private repository, make sure Kubernetes has access with the correct credentials.

2. **Error: `kubectl command not found`**
   - Ensure that `kubectl` is installed and in your system's PATH.

3. **Error: `Helm release already exists`**
   - Use the `helm upgrade` command to update the deployment.
