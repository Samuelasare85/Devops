FROM node:17-alpine

RUN npm install -g nodemon

# WORKDIR /the/workdir/path
WORKDIR /app

COPY package.json .

RUN npm install 

# COPY source dest
COPY . .  

# EXPOSE port
EXPOSE 4000

# CMD [ "executable" ]
CMD ["npm", "run", "dev"]