FROM python:3.10-slim

# Sistem bağımlılıklarını kur
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxrender1 libxext6 gcc g++ build-essential \
    && apt-get clean

# Çalışma klasörünü ayarla
WORKDIR /app

# Gereksinim dosyasını kopyala ve yükle
COPY requirements.txt .
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Python dosyasını kopyala
COPY main.py .

# Çalıştırılacak komut
# CMD ["python", "main.py"]
