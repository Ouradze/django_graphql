FROM node:latest

RUN mkdir /demo

WORKDIR /demo

# add `/frontend/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

COPY ./frontend/ /demo/

RUN npm install

COPY ./compose/frontend/run_front.sh /

CMD /run_front.sh
