# base image
FROM python:3.8

ARG CONKEY=test
ARG CONSEC=test
ARG ACCTOK=test
ARG ACCSEC=test


# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY . .  

# set twitter API tokens
RUN cp src/configs.example src/configs
RUN export CONKEY=$CONKEY && sed -i 's/##Your APP ConsumerKey##/'"${CONKEY}"'/g' src/configs
RUN export CONSEC=$CONSEC && sed -i 's/##Your APP ConsumerSecret##/'"${CONSEC}"'/g' src/configs
RUN export ACCTOK=$ACCTOK && sed -i 's/##Your APP AccessToken##/'"${ACCTOK}"'/g' src/configs
RUN export ACCSEC=$ACCSEC && sed -i 's/##Your APP AccessSecret##/'"${ACCSEC}"'/g' src/configs
# install dependencies
RUN pip install -r requirements.txt

# command to run on container start within prompt
CMD [ "/bin/bash" ]

