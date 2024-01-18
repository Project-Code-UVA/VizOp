import React from 'react';
import Plot from 'react-plotly.js';

class SampleGraph extends React.Component {
  render() {
    return (
      <div className="sample-graph">
        <Plot
          data={[{
            x: [1, 2, 3],
            y: [4, 5, 6],
            z: [7, 8, 9],
            type: 'scatter3d',
            mode: 'lines+markers',
            marker: {color: 'red'},
          }]}
          layout={ {autosize: true, title: 'A Fancy Plot', scene: {bgcolor: 'lightblue'}} }
        />
      </div>
    );
  }
}

export default SampleGraph;