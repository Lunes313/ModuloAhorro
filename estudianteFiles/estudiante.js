document.addEventListener("DOMContentLoaded", function() {
    fetch('http://127.0.0.1:5000/datos')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Actualizar el total de presupuesto
            document.getElementById('presupuesto_usuario').textContent = `$${data.presupuesto_total}`;

            // Actualizar el total de gastos
            document.getElementById('total_gastos').textContent = `$${data.gastado}`;

            // Calcular y mostrar el porcentaje de gastos sobre el presupuesto
            var porcentaje = 0;
            if (data.presupuesto_total > 0) {
                porcentaje = (data.gastado / data.presupuesto_total) * 100;
            }
            document.getElementById('porcentaje').textContent = porcentaje.toFixed(2) + '%';
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
