# Sistema de Gestión Veterinaria "Amigos Peludos" 

## Descripción
Sistema de gestión para la Clínica Veterinaria "Amigos Peludos", desarrollado en Python. Esta aplicación permite administrar el registro de mascotas, sus dueños y el historial de consultas médicas, facilitando la gestión diaria de la clínica veterinaria.

## Características Principales 
- Registro completo de mascotas y sus dueños
- Gestión de consultas veterinarias
- Visualización de historiales médicos
- Listado de mascotas registradas

## Estructura del Proyecto 
El proyecto está organizado en los siguientes módulos:
- `Veterinaria.py`: Módulo principal con el menú y funciones core
- `Animales.py`: Gestión de mascotas
- `Personas.py`: Gestión de dueños
- `Historias.py`: Gestión de consultas médicas

## Funcionalidades Detalladas 

### 1. Registro de Mascotas
- Nombre de la mascota
- Especie
- Raza
- Edad
- Información del dueño

### 2. Registro de Dueños
- Nombre completo
- Teléfono de contacto
- Dirección

### 3. Gestión de Consultas
- Fecha de la consulta
- Motivo de la visita
- Diagnóstico veterinario
- Registro asociado a la mascota

### 4. Consulta de Información
- Listado completo de mascotas
- Datos de contacto de dueños
- Historial médico por mascota

La aplicación tiene en cuenta que un dueño puede tener 1 o mas mascotas y con esta lógica se presenta el 
proyecto, además al registrar una consulta, se necesita tener ya la mascota registrada o sino no se podrá registrar
Si se registra la misma mascota y el mismo dueño, el programa muestra un mensaje diciendo que ya esta registrada la 
mascota.

## Autor 
Alejandro Botero Raigosa