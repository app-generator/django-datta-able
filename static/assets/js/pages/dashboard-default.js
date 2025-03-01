'use strict';
// [ world-low chart ] start
(function () {
    var map = new jsVectorMap({
        selector: "#world-low",
        map: "world",
        markersSelectable: true,
        markers: [{
                coords: [-14.2350, -51.9253]
            },
            {
                coords: [35.8617, 104.1954]
            },
            {
                coords: [61, 105]
            },
            {
                coords: [26.8206, 30.8025]
            }
        ],
        markerStyle: {
            initial: {
                fill: '#3f4d67',

            },
            hover: {
                fill: '#04a9f5',
            },
        },
        markerLabelStyle: {
            initial: {
                fontFamily: "'Inter', sans-serif",
                fontSize: 13,
                fontWeight: 500,
                fill: '#3f4d67',
            },
        },
    });
})();
// [ world-low chart ] end

// [ Widget-line-chart ] start
var options = {
    chart: {
        type: 'line',
        height: 210,
        zoom: {
            enabled: false
        },
        toolbar: {
            show: false,
        },
    },
    dataLabels: {
        enabled: false,
    },
    colors: ["#fff"],
    fill: {
        type: 'solid',
    },
    plotOptions: {
        bar: {
            columnWidth: '30%',
        }
    },
    series: [{
        data: [10, 60, 45, 72, 45, 86]
    }],
    xaxis: {
        categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        axisBorder: {
            show: false,
        },
        axisTicks: {
            show: false,
        },
        labels: {
            style: {
                colors: "#fff"
            }
        },
    },
    yaxis: {
        axisBorder: {
            show: false,
        },
        axisTicks: {
            show: false,
        },
        crosshairs: {
            width: 0
        },
        labels: {
            show: false,
        },
    },
    grid: {
        padding: {
            bottom: 0,
            left: 10,
        },
        xaxis: {
            lines: {
                show: false
            }
        },
        yaxis: {
            lines: {
                show: false
            }
        },
    },
    markers: {
        size: 5,
        colors: '#fff',
        opacity: 0.9,
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    tooltip: {
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return 'Statistics :'
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#Widget-line-chart"), options);
chart.render();
// [ Widget-line-chart ] end