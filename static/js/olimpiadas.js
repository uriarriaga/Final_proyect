function olimpiadas(response) {
    // console.log(response)

var trace1 = {
    x: response.map(i => i.month),
    y: response.map(i => i.total_count),
    name: 'yaxis data',
    yaxis: 'y1',
    type: 'bar'
  };
  
  var trace2 = {
    x: response.map(i => i.month),
    y: response.map(i => i.nsat),
    yaxis: 'y2',
    mode: 'lines'
  };
   
  var data = [trace1, trace2];
  
  var layout = {
    // title:'Line and Scatter Plot'
    yaxis: {title: 'yaxis title'},
    yaxis2: {
        title: 'yaxis2 title',
        overlaying: 'y',
        side: 'right'}
  };
  
  Plotly.newPlot('olimpiadas', data, layout);

};

d3.json("/olimpiadas").then(olimpiadas);