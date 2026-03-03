document.addEventListener("DOMContentLoaded", function () {

    // Get values from HTML
    let total = parseInt(document.querySelectorAll(".card p")[0].innerText);
    let disease = parseInt(document.querySelectorAll(".card p")[1].innerText);
    let healthy = parseInt(document.querySelectorAll(".card p")[2].innerText);

    // Create Chart
    const ctx = document.getElementById('chart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',

        data: {
            labels: ['Total', 'Disease', 'Healthy'],

            datasets: [{
                label: 'Statistics',

                data: [total, disease, healthy],

                borderWidth: 2
            }]
        },

        options: {

            responsive: true,

            plugins: {
                legend: {
                    display: true
                }
            },

            scales: {
                y: {
                    beginAtZero: true
                }
            }

        }

    });

});