# Dockerfile
FROM node:alpine
# directorio dentro del contenedor para el código
WORKDIR /urs/src/app  
COPY package*.json ./
RUN npm ci
COPY . .
CMD ["npm", "start"]
