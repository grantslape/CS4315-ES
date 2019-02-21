# BASE IMAGE
FROM node:11.10.0

# SET WORK DIR
# this might not be correct (check path)
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Add node binaries to path
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install dependencies
COPY package.json /usr/src/app/package.json
RUN npm install && npm install react-scripts@1.1.1 -g

# ENTRYPOINT
CMD ["npm", "start"]