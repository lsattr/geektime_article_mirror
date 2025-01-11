FROM registry.cn-shenzhen.aliyuncs.com/lsattr/node:18-alpine

WORKDIR /app

RUN npm install -g markdown-http-server

VOLUME ["/web"]

EXPOSE 7070

CMD ["markdown-server", "/web", "-p", "7070"]
