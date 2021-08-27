function twitter_stacked(response) {
    // console.log(response)

    response.forEach(element => {
        element.total = element.positive+element.negative+element.neutral
        element.ppositive = element.positive/element.total
        element.pnegative = element.negative/element.total
        element.pneutral = element.neutral/element.total
    });
    
    console.log(response)

    var tracepositive = {
        x: response.map(i => i.ppositive),
        y: response.map(i => i.key_word),
        name: 'Positive',
        orientation: 'h',
        marker: {
            color: 'rgba(11,156,49,0.6)',
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
            color: 'rgba(255,0,0,0.6)',
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
            color: 'rgba(255,231,32,0.6)',
            width: 1
        }
    };

    var data = [tracepositive, traceneutral, tracenegative];

    var layout = {
        title: 'Twitter Stacked',
        barmode: 'stack'
    };

    Plotly.newPlot('twitter_stacked', data, layout);

};

d3.json("/static/js/twitter_stacked.json").then(twitter_stacked);
