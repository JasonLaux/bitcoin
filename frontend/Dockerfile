FROM node:18.4.0

WORKDIR /frontend

COPY package.json /frontend

RUN npm install

COPY . /frontend

CMD ["npm", "start"]