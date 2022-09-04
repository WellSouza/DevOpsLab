#cria imagem inicial
FROM python:rc-slim

#Diretrorio de trabalho
WORKDIR /app

#Copiar a aplicação para pasta
COPY . /app

#Instalar depencdencias
RUN pip install --trusted-host pype.phyton.org -r requirements.txt

#Inciar a aplicaação
CMD ["gunicorn","app:app"]