#utilisation d'une image de base Ubuntu
FROM ubuntu:20.04

#Mettre à jour Ubuntu Software repository

RUN apt-get update 

#Installation de Java 
RUN apt-get install -y openjdk-11-jdk

#Ajout de variables d'environnement pour Java 
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64/
RUN export JAVA_HOME

# Téléchargement de Hadoop 
RUN apt-get install -y wget 
RUN wget https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz

# Décompression de Hadoop
RUN tar -xvf hadoop-3.3.1.tar.gz
RUN mv hadoop-3.3.1 /usr/local/hadoop

# Ajout de variables d'environnement pour Hadoop
ENV HADOOP_HOME /usr/local/hadoop
ENV PATH $PATH:$HADOOP_HOME/bin
RUN export HADOOP_HOME PATH

# Création de répertoires nécessaires pour HDFS
RUN mkdir -p $HADOOP_HOME/hdfs/namenode
RUN mkdir -p $HADOOP_HOME/hdfs/datanode

# Copie des fichiers de configuration (supposant qu'ils se trouvent dans le répertoire courant)
COPY core-site.xml $HADOOP_HOME/etc/hadoop/
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/

# Formatage du namenode
RUN $HADOOP_HOME/bin/hdfs namenode -format

# Exposition des ports nécessaires (à adapter à vos besoins)
EXPOSE 50070
EXPOSE 50075
EXPOSE 50090
EXPOSE 8088
EXPOSE 19888
EXPOSE 8030
EXPOSE 8031
EXPOSE 8032
EXPOSE 8033
EXPOSE 8040
EXPOSE 8042
EXPOSE 22
EXPOSE 9000

# Commande par défaut à l'exécution du conteneur
CMD [ "/usr/sbin/sshd", "-D" ]

#Supprimer les packages inutiles 
RUN apt-get purge 