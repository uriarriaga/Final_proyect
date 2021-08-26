function nsat2 (response) {
    // console.log(response)

var trace1 = {
    x: response.map(i => i.year),
    y: response.map(i => i.total_count),
    name: 'Tweets Count',
    yaxis: 'y1',
    type: 'bar'
  };
  
  var trace2 = {
    x: response.map(i => i.year),
    y: response.map(i => i.nsat),
    name: 'NSAT',
    yaxis: 'y2',
    mode: 'lines'
  };
   
  var data = [trace1, trace2];
  
  var layout = {
    // title:'Line and Scatter Plot'
    showlegend: false,
    xaxis: {
      tickmode: "linear", //  If "linear", the placement of the ticks is determined by a starting position `tick0` and a tick step `dtick`
      tick0: 0,
      dtick: 1
    },
    yaxis: {title: 'Tweet Count (bar)', showgrid: false },
    yaxis2: {
        title: 'NSAT (line)',
        overlaying: 'y',
        range: [0, 0.5],
        side: 'right'}
  };
  
  Plotly.newPlot('nsat2', data, layout);

};

d3.json("/nsat2").then(nsat2);