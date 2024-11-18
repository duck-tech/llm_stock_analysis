# llama

llama images

- docker pull ilopezluna/llama3.1:0.3.14-8b
- docker pull ollama/ollama

-  docker run --rm -d -p 11434:11434 -it --name llama3.1 docker.io/ilopezluna/llama3.1:0.3.14-8b
-  docker exec -it llama3.1 ollama list