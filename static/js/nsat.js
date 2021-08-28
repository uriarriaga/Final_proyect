function nsat(response) {
    // console.log(response)


    var xValue = response.filter(i => i.key_word !== "OLIMPIADAS").map(i => i.key_word);

    var yValue = response.filter(i => i.key_word !== "OLIMPIADAS").map(i => i.nsat);

    var trace1 = {
        x: xValue,
        y: yValue,
        type: 'bar',
        text: yValue.map(String),
        textposition: 'auto',
        hoverinfo: 'none',
        marker: {
            color: 'rgb(158,202,225)',
            opacity: 0.6,
            line: {
                color: 'rgb(8,48,107)',
                width: 1.5
            }
        }
    };

    var data = [trace1];

    var layout = {
        title: null, 
        barmode: 'stack'
    };

    Plotly.newPlot('nsat', data, layout);

};

d3.json("/nsat").then(nsat);