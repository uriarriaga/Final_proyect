function time_nsat(response) {
    // console.log(response)

    var xData = [response.filter(i => i.key_word === "Netflix").map(i => i.year),
                response.filter(i => i.key_word === "Amazon Prime Video").map(i => i.year),
                response.filter(i => i.key_word === "HBO Max").map(i => i.year),
                response.filter(i => i.key_word === "Paramount+").map(i => i.year),
                response.filter(i => i.key_word === "Blim").map(i => i.year),
                response.filter(i => i.key_word === "Star Plus").map(i => i.year),
                response.filter(i => i.key_word === "Disney +").map(i => i.year)];
    // console.log(xData)

    var yData = [response.filter(i => i.key_word === "Netflix").map(i => i.nsat),
                response.filter(i => i.key_word === "Amazon Prime Video").map(i => i.nsat),
                response.filter(i => i.key_word === "HBO Max").map(i => i.nsat),
                response.filter(i => i.key_word === "Paramount+").map(i => i.nsat),
                response.filter(i => i.key_word === "Blim").map(i => i.nsat),
                response.filter(i => i.key_word === "Star Plus").map(i => i.nsat),
                response.filter(i => i.key_word === "Disney +").map(i => i.nsat)];
    // console.log(yData)

    var colors = ['rgba(67,67,67,1)', 'rgba(115,115,115,1)', 'rgba(49,130,189, 1)',
        'rgba(189,189,189,1)', 'rgba(241,130,141,1)', 'rgba(82,179,217,1)', 'rgba(243,156,18,1)'
    ];

    var lineSize = [2, 2, 2, 2, 2, 2, 2];

    var labels = ["Netflix", "Amazon Prime Video", "HBO Max", "Paramount+", "Blim", "Star Plus", "Disney +"];

    var data = [];

    for (var i = 0; i < xData.length; i++) {
        var result = {
            x: xData[i],
            y: yData[i],
            type: 'scatter',
            mode: 'lines',
            line: {
                color: colors[i],
                width: lineSize[i]
            }
        };
        var result2 = {
            x: [xData[i][0], xData[i][11]],
            y: [yData[i][0], yData[i][11]],
            type: 'scatter',
            mode: 'markers',
            marker: {
                color: colors[i],
                size: 12
            }
        };
        data.push(result, result2);
    }

    var layout = {
        showlegend: false,
        height: 600,
        width: 600,
        xaxis: {
            showline: true,
            showgrid: false,
            showticklabels: true,
            linecolor: 'rgb(204,204,204)',
            linewidth: 2,
            autotick: false,
            ticks: 'outside',
            tickcolor: 'rgb(204,204,204)',
            tickwidth: 2,
            ticklen: 5,
            tickfont: {
                family: 'Arial',
                size: 12,
                color: 'rgb(82, 82, 82)'
            }
        },
        yaxis: {
            showgrid: false,
            zeroline: false,
            showline: false,
            showticklabels: false
        },
        autosize: false,
        margin: {
            autoexpand: false,
            l: 100,
            r: 100,
            t: 20
        },
        annotations: [
            {
                xref: 'paper',
                yref: 'paper',
                x: 0.5,
                y: -0.1,
                xanchor: 'center',
                yanchor: 'top',
                text: 'Source: Twitter API',
                showarrow: false,
                font: {
                    family: 'Arial',
                    size: 12,
                    color: 'rgb(150,150,150)'
                }
            }
        ]
    };

    for (var i = 0; i < xData.length; i++) {
        var result = {
            xref: 'paper',
            x: 0.05,
            y: yData[i][0],
            xanchor: 'right',
            yanchor: 'middle',
            text: labels[i] + ' ' + yData[i][0] + '%',
            showarrow: false,
            font: {
                family: 'Arial',
                size: 16,
                color: 'black'
            }
        };
        var result2 = {
            xref: 'paper',
            x: 0.95,
            y: yData[i][11],
            xanchor: 'left',
            yanchor: 'middle',
            text: yData[i][11] + '%',
            font: {
                family: 'Arial',
                size: 16,
                color: 'black'
            },
            showarrow: false
        };

        layout.annotations.push(result, result2);
    }

    Plotly.newPlot('time_nsat', data, layout);

};

d3.json("/static/js/time_nsat.json").then(time_nsat);