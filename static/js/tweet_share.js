
function tweet_share(response) {
    // console.log(response)

    var data = [{
        type: "pie",
        values: response.filter(i => i.key_word !== "OLIMPIADAS").map(i => i.total_count),
        labels: response.filter(i => i.key_word !== "OLIMPIADAS").map(i => i.key_word),
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

d3.json("/tweet_share").then(tweet_share);
