# docker-jim-p3

---

```
cd project

docker build -t flask-jim .

docker run --name flask-app -p 5000:5000 -e DEBUG=1 flask-jim

docker compose up --build

docker compose down --rmi "local"

docker compose ps

```