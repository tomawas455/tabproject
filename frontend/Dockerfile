FROM node:17-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
EXPOSE 3000
RUN npm install
RUN chown -R node /usr/src/app/node_modules
CMD ["npm", "start"]
