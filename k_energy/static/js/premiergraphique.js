
document.addEventListener("DOMContentLoaded", function(){
    const ctx = document.getElementById('myFirstChart').getContext('2d');
              new Chart(ctx, {
                type: 'line',
                data: {
                  labels: [1,2, 3,4, 5, 6,7, 8, 9, 10, 11, 12],
                  datasets : [
                    {
                      label: 'Consommation (kWh)',
                      data : [100, 200, 400, 300, 700, 800, 600, 700, 500, 400, 800, 900],
                      pointBackgroundColor: '#173b61',
                      borderColor:'#173b61',
                      borderWidth: 2,
                      tension : 0.4
                    }
                  ]
                },
              options: {
                responsive: true,
                plugins: {
                  legend: {
                    display: true,
                    position : 'top',
                  },
                },
                scales: {
                  y : {
                    beginAtZero: true
                  },
                },
              },
              });
          }
  
);