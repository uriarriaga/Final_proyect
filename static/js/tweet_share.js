
function tweet_share(response) {
    // console.log(response)

    var data = [{
        type: "pie",
        values: response.map(i => i.total_count),
        labels: response.map(i => i.key_word),
        textinfo: "label+percent",
        textposition: "outside",
        automargin: true
    }]

    var layout = {
        height: 400,
        width: 400,
        margin: { "t": 0, "b": 0, "l": 0, "r": 0 },
        showlegend: false
    }

    Plotly.newPlot('tweet_share', data, layout);

};

d3.json("/static/js/tweet_share.json").then(tweet_share);
