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
    d3.csv('/optionsTradeData.csv').then((data) => {
      const aaplData = data.filter((row) => row.Sym === 'AAPL');
      
      const graphData = {
        x: aaplData.map((row) => row.Strike),
        y: aaplData.map((row) => row.StockPrice),
        mode: 'markers',
        type: 'scatter',
      };

      const dummyData = {
        x: [200.0,197.5,200.0,200.0,197.5,202.5,202.5,195.0,197.5,202.5,200.0,200.0,190.0,187.5,187.5,220.0,187.5],
        y: [200.1,200.03,199.83,199.87,199.32,202.0,202.0,202.21,196.33,198.47,197.97,196.48,196.12,195.31,195.31,196.28,196.18],
        mode: 'markers',
        type: 'scatter',
      }

      this.setState({ dummyData });
    });
  }

  render() {
    const { dummyData } = this.state;
  
    return (
      <div>
        <Plot data={[dummyData]} layout={{ title: 'AAPL Option Strike Price vs. Stock Price' }} />
      </div>
    );
  }  
}

export default SampleGraph;