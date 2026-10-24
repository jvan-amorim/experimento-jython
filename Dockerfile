# Setup Java + Jython
FROM eclipse-temurin:17-jre
ENV JYTHON_VERSION=2.7.3
ADD https://repo1.maven.org/maven2/org/python/jython-standalone/${JYTHON_VERSION}/jython-standalone-${JYTHON_VERSION}.jar /opt/jython/jython.jar
WORKDIR /app
COPY exemplo1.py exemplo2.py ./

# Executa os dois scripts em sequencia
CMD ["sh", "-c", "java -jar /opt/jython/jython.jar exemplo1.py && java -jar /opt/jython/jython.jar exemplo2.py"]
