
# Laravel Dockerized Application

This repository contains a Laravel application containerized with Docker and Docker Compose. Follow the steps below to build, set up, and run the application.

---

## Prerequisites

Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Steps to Run the Application

### 1. Set Up Environment Variables

Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

Update the `.env` file with the following database configuration:
```env
DB_CONNECTION=mysql
DB_HOST=db
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=laravel
DB_PASSWORD=secret

SESSION_DRIVER=database
```

---

### 2. Build and Start the Containers

Run the following command to build the Docker images and start the containers:
```bash
docker-compose up -d --build
```

---

### 3. Install Laravel Dependencies

Access the Laravel application container and install dependencies using Composer:
```bash
docker-compose exec app bash
composer install
```

---

### 4. Set Up Laravel

#### Generate the Application Key
Run this command to generate the application key:
```bash
php artisan key:generate
```

#### Run Database Migrations
Run the database migrations to set up the database schema:
```bash
php artisan migrate
```

---

### 5. Set Permissions

Ensure the `storage` and `bootstrap/cache` directories are writable by running:
```bash
chmod -R 775 storage bootstrap/cache
```

This ensures Laravel can write to the necessary directories.

---

### 6. Access the Application

Once the setup is complete, visit the application in your browser at:

http://localhost:8000
