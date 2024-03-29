$(document).ready(function() {
    transitionSideBar();
    main_Chart();
    accountRec_Chart();
    taskChart();
});

function update_Main_Chart_Sub_Data() {
    $("#userPostingCount").html("5");

}

function transitionSideBar() {
    document.getElementsByClassName('col-md-2 d-none d-md-block bg-light sidebar')[0].style.setProperty('display', 'none', 'important');
    document.getElementsByClassName('col-md-10 col-lg-10')[0].className = 'col-lg-auto'
}



function main_Chart() {
    var numberWithCommas = function(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    };
    var dataPack1 = [40, 20]; //Note to self -- to utilize AJAX get call to dynamically return data
    var dataPack2 = [10, 0];
    var dates = ["Support Uploaded", "Support Not Uploaded"];

    var bar_ctx = document.getElementById('journalentry-chart');
    var bar_chart = new Chart(bar_ctx, {
        type: 'horizontalBar',
        data: {
            labels: dates,
            datasets: [{
                    label: 'Not Approved',
                    data: dataPack1,
                    backgroundColor: "#778899",
                    hoverBackgroundColor: "#778899",
                    hoverBorderWidth: 0
                },
                {
                    label: 'Approved',
                    data: dataPack2,
                    backgroundColor: "#20a8d8",
                    hoverBackgroundColor: "#20a8d8",
                    hoverBorderWidth: 0
                },
            ]
        },
        options: {
            animation: {
                duration: 10,
            },
            tooltips: {
                mode: 'label',
                callbacks: {
                    label: function(tooltipItem, data) {
                        return data.datasets[tooltipItem.datasetIndex].label + ": " + numberWithCommas(tooltipItem.yLabel);
                    }
                }
            },
            scales: {
                xAxes: [{
                    stacked: true,
                    gridLines: { display: false },
                }],
                yAxes: [{
                    stacked: true,
                    ticks: {
                        callback: function(value) { return numberWithCommas(value); },
                    },
                }],
            }, // scales
            legend: { display: true }
        } // options
    });
};

function accountRec_Chart() {
    var numberWithCommas = function(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    };
    var dataPack1 = [40, 20]; //Note to self -- to utilize AJAX get call to dynamically return data
    var dataPack2 = [10, 0];
    var dates = ["Support Uploaded", "Support Not Uploaded"];

    var bar_ctx = document.getElementById('accountrec-chart');
    bar_chart = new Chart(bar_ctx, {
        type: 'horizontalBar',
        data: {
            labels: dates,
            datasets: [{
                    label: 'Not Approved',
                    data: dataPack1,
                    backgroundColor: "#778899",
                    hoverBackgroundColor: "#778899",
                    hoverBorderWidth: 0
                },
                {
                    label: 'Approved',
                    data: dataPack2,
                    backgroundColor: "#20a8d8",
                    hoverBackgroundColor: "#20a8d8",
                    hoverBorderWidth: 0
                },
            ]
        },
        options: {
            animation: {
                duration: 10,
            },
            tooltips: {
                mode: 'label',
                callbacks: {
                    label: function(tooltipItem, data) {
                        return data.datasets[tooltipItem.datasetIndex].label + ": " + numberWithCommas(tooltipItem.yLabel);
                    }
                }
            },
            scales: {
                xAxes: [{
                    stacked: true,
                    gridLines: { display: false },
                }],
                yAxes: [{
                    stacked: true,
                    ticks: {
                        callback: function(value) { return numberWithCommas(value); },
                    },
                }],
            }, // scales
            legend: { display: true }
        } // options
    });
};

function taskChart() {
    var numberWithCommas = function(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    };
    var dataPack1 = [40, 20]; //Note to self -- to utilize AJAX get call to dynamically return data
    var dataPack2 = [10, 0];
    var dates = ["Support Uploaded", "Support Not Uploaded"];

    var bar_ctx = document.getElementById('task-chart');
    bar_chart = new Chart(bar_ctx, {
        type: 'horizontalBar',
        data: {
            labels: dates,
            datasets: [{
                    label: 'Not Approved',
                    data: dataPack1,
                    backgroundColor: "#778899",
                    hoverBackgroundColor: "#778899",
                    hoverBorderWidth: 0
                },
                {
                    label: 'Approved',
                    data: dataPack2,
                    backgroundColor: "#20a8d8",
                    hoverBackgroundColor: "#20a8d8",
                    hoverBorderWidth: 0
                },
            ]
        },
        options: {
            animation: {
                duration: 10,
            },
            tooltips: {
                mode: 'label',
                callbacks: {
                    label: function(tooltipItem, data) {
                        return data.datasets[tooltipItem.datasetIndex].label + ": " + numberWithCommas(tooltipItem.yLabel);
                    }
                }
            },
            scales: {
                xAxes: [{
                    stacked: true,
                    gridLines: { display: false },
                }],
                yAxes: [{
                    stacked: true,
                    ticks: {
                        callback: function(value) { return numberWithCommas(value); },
                    },
                }],
            }, // scales
            legend: { display: true }
        } // options
    });
};