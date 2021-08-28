function olimpiadas(response) {
    // console.log(response)

var trace1 = {
    x: response.map(i => i.month),
    y: response.map(i => i.total_count),
    name: 'Tweets Count',
    yaxis: 'y1',
    type: 'bar'
  };
  
  var trace2 = {
    x: response.map(i => i.month),
    y: response.map(i => i.nsat),
    name: 'NSAT',
    yaxis: 'y2',
    mode: 'lines'
  };
   
  var data = [trace1, trace2];
  
  var layout = {
    // title:'Line and Scatter Plot'
    showlegend: false,
    yaxis: {title: 'Tweet Count (bar)', showgrid: false},
    yaxis2: {
        title: 'NSAT (line)',
        overlaying: 'y',
        range: [0, 0.5],
        side: 'right'}
  };
  
  Plotly.newPlot('olimpiadas', data, layout);

};

d3.json("/olimpiadas").then(olimpiadas);