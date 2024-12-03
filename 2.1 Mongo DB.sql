// Conectar y crear la colección 'Estudiantes'
db.Estudiantes.insertMany([
    { "nombre": "Maria", "edad": 22, "ciudad": "Bogotá" },
    { "nombre": "Anai", "edad": 72, "ciudad": "Medellín" },
    { "nombre": "Mauricio", "edad": 29, "ciudad": "Cali" }
]);

// Consultar todos los documentos de la colección
db.Estudiantes.find();

// Filtrar estudiantes por ciudad
db.Estudiantes.find({ "ciudad": "Medellín" });

// Consultar estudiantes mayores de 20 años
db.Estudiantes.find({ "edad": { $gt: 20 } });
