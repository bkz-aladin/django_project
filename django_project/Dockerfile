# Base image
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# install dependencies  
RUN pip install --upgrade pip  

# Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Expose port 8000 for the Django development server
EXPOSE 5000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]