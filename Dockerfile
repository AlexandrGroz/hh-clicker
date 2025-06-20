# Base image
FROM python:3.12-slim

# System libraries required for Google Chrome (headless or GUI)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget gnupg ca-certificates \
        fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 \
        libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 \
        libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 \
        libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 \
        libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 \
        libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
        libxss1 libxtst6 zlib1g libgdk-pixbuf2.0-0 libffi8 && \
    rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -qO- https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends google-chrome-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Display variable (ignored in headless mode)
ENV DISPLAY=:99

# Working directory
WORKDIR /app

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code
COPY . .

# Entrypoint
CMD ["python", "script.py"]
