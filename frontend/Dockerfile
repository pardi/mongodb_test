FROM node:21-alpine3.18

WORKDIR /app

COPY app/ .

RUN npm install --save-dev typescript 
RUN npx tsc

CMD ["npm", "start"]