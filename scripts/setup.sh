
echo “Building Docker image...”
docker build -t my-app:latest ./app

echo “Deploying with Helm...”
helm upgrade --install my-app ./helm-chart

echo “Pods status...”
kubectl get pods