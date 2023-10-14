import React, { Component } from 'react';
import Plot from 'react-plotly.js';
import * as d3 from 'd3';

class SampleGraph extends Component {
  constructor() {
    super();
    this.state = {
      graphData: [],
    };
  }

  componentDidMount() {
    d3.csv('optionsTradeData.csv').then((data) => {
        console.log(data);
      const aaplData = data.filter((row) => row.Sym === 'AAPL');
      
      const graphData = {
        x: aaplData.map((row) => row.Strike),
        y: aaplData.map((row) => row.StockPrice),
        mode: 'markers',
        type: 'scatter',
      };

      this.setState({ graphData });
    });
  }

  render() {
    const { graphData } = this.state;
  
    return (
      <div>
        <Plot data={[graphData]} layout={{ title: 'AAPL Option Strike Price vs. Stock Price' }} />
      </div>
    );
  }  
}

export default SampleGraph;