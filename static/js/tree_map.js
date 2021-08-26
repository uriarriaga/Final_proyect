function tree_map(response) {
    positive = response.filter(i => i.mood ==='+')
    neutral = response.filter(i => i.mood ==='n')
    negative = response.filter(i => i.mood ==='-')

    data = [{
        type: "treemap",
        labels: ["words", "positive", "neutral", "Negative"],
        parents: ["", "words", "words", "words"]
    }]

    positive.forEach(element => {
        data[0]['labels'].push(element.word);
        data[0]['parents'].push('positive');
    });

    neutral.forEach(element => {
        data[0]['labels'].push(element.word);
        data[0]['parents'].push('neutral');
    });

    negative.forEach(element => {
        data[0]['labels'].push(element.word);
        data[0]['parents'].push('negative');
    });
    

    Plotly.newPlot('tree_map', data)
};
d3.json("/tree_map").then(tree_map);
