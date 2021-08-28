function twitter_stacked(response) {
    // console.log(response)

    response.forEach(element => {
        element.total = element.positive+element.negative+element.neutral
        element.ppositive = element.positive/element.total
        element.pnegative = element.negative/element.total
        element.pneutral = element.neutral/element.total
    });
    
    // console.log(response)

    var tracepositive = {
        x: response.map(i => i.ppositive),
        y: response.map(i => i.key_word),
        name: 'Positive',
        orientation: 'h',
        marker: {
            color: 'rgba(0,184,148,0.6)',
            width: 1
        },
        type: 'bar'
    };

    var tracenegative = {
        x: response.map(i => i.pnegative),
        y: response.map(i => i.key_word),
        name: 'Negative',
        orientation: 'h',
        type: 'bar',
        marker: {
            color: 'rgba(246,71,71,0.6)',
            width: 1
        }
    };

    var traceneutral = {
        x: response.map(i => i.pneutral),
        y: response.map(i => i.key_word),
        name: 'Neutral',
        orientation: 'h',
        type: 'bar',
        marker: {
            color: 'rgba(116,185,255,0.6)',
            width: 1
        }
    };

    var data = [tracepositive, traceneutral, tracenegative];

    var layout = {
        title: null,
        barmode: 'stack'
    };

    Plotly.newPlot('twitter_stacked', data, layout);

};

d3.json("/twitter_stacked").then(twitter_stacked);
