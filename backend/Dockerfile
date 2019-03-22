# BASE IMAGE
ARG PYTHON_VERSION=3.7.2
FROM python:${PYTHON_VERSION}-alpine3.9

# Add requirements first
RUN mkdir /usr/src/backend
ADD app/requirements.txt /usr/src/backend/

# Set the working directory to /app
WORKDIR /usr/src/backend

# Install dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Open port 5000
EXPOSE 5000

# Copy the app into the container at /app
ADD app /usr/src/backend

ENTRYPOINT [ "python" ]

CMD ["src/app.py"]