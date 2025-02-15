rm -rf ./frontend/dist/*
npm i
npm run build
docker-compose down
docker-compose build
docker-compose up
