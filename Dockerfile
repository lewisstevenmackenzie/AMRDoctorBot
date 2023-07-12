# FROM python:3.10

# RUN python -m pip install rasa

# WORKDIR /app
# COPY . .

# RUN rasa train nlu

# USER 1001

# ENTRYPOINT [ "rasa" ]

# CMD [ "run", "--enable-api", "--port" ,"8080" ]


# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.6.0

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
# RUN pip install -r requirements-actions.txt
RUN python -m pip install rasa

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001