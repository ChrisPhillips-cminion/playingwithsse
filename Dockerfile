FROM python

WORKDIR /app


# install simple http server for serving static content
RUN npm install ws sleep
# make the 'app' folder the current working directory

# copy both 'package.json' and 'package-lock.json' (if available)
COPY server.py ./

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .


USER 1000

EXPOSE 8080
CMD [ "python3", "server.py"]
