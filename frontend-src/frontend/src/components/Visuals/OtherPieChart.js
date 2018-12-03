import React, { PureComponent } from 'react';
import fp from 'lodash/fp';
import ReactD3PieChart from './ReactD3PieChart';

class PieChart extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      data: [
         {
            label: "January",
            value: 77
         },
         {
            label: "February",
            value: 57
         },
         {
            label: "March",
            value: 75
         },
         {
            label: "April",
            value: 36
         },
         {
            label: "May",
            value: 5
         },
         {
            label: "June",
            value: 7
         },
         {
            label: "July",
            value: 2
         },
         {
            label: "August",
            value: 4
         },
         {
            label: "September",
            value: 7
         },
         {
            label: "October",
            value: 58
         },
         {
            label: "November",
            value: 1000
         },
         {
            label: "December",
            value: 447
         }
      ],
    };
  }

  handleClick = () => {
    const lastData = fp.last(this.state.data);
    const { label } = lastData;
    const newLabel = String.fromCharCode(label.charCodeAt() + 1);
    const newValue = Math.floor(Math.random() * 31);

    this.setState({
      data: [
        ...this.state.data,
        { label: newLabel, value: newValue },
      ],
    });
  }

  renderLabel = d => `${d.data.label}`

  render() {
    return (
        <div className="container">
        <ReactD3PieChart data={this.state.data} tooltip renderLabel={this.renderLabel} />
        </div>
    );
  }

}

export default PieChart;
