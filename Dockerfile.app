FROM node:18-alpine as build
WORKDIR /app
COPY ./frontend/package.json ./frontend/yarn.lock ./
COPY ./frontend/src ./src
COPY ./frontend/public ./public
COPY ./frontend/tsconfig.json ./
RUN yarn install
RUN yarn build

FROM python:3.9.13 as app
WORKDIR /app
RUN mkdir build
COPY --from=build /app/build ./build
RUN mkdir api
COPY ./backend ./api
RUN pip install -r ./api/requirements.txt
WORKDIR /app/api
CMD [ "python", "index.py" ]


