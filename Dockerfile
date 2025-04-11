FROM python

WORKDIR /app


# install simple http server for serving static content
# make the 'app' folder the current working directory
RUN pip install aiohttp-sse
# copy both 'package.json' and 'package-lock.json' (if available)
COPY server.py ./

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .


USER 1000

EXPOSE 8080
CMD [ "python3", "server.py"]
