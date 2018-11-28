import React, { PureComponent } from 'react';
import fp from 'lodash/fp';
import ReactD3PieChart from './ReactD3PieChart';

class PieChart extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      data: [
         {
            label: "A",
            value: 6,
            color: "#2484c1"
         },
         {
            label: "B",
            value: 22,
            color: "#0c6197"
         },
         {
            label: "C",
            value: 14,
            color: "#4daa4b"
         },
         {
            label: "D",
            value: 9,
            color: "#90c469"
         },
         {
            label: "E",
            value: 4,
            color: "#daca61"
         },
         {
            label: "G",
            value: 9,
            color: "#e98125"
         },
         {
            label: "H",
            value: 3,
            color: "#cb2121"
         },
         {
            label: "I",
            value: 2,
            color: "#830909"
         },
         {
            label: "J",
            value: 1,
            color: "#923e99"
         },
         {
            label: "K",
            value: 2,
            color: "#ae83d5"
         },
         {
            label: "L",
            value: 4,
            color: "#bf273e"
         },
         {
            label: "M",
            value: 1,
            color: "#ce2aeb"
         },
         {
            label: "N",
            value: 3,
            color: "#bca44a"
         },
         {
            label: "O",
            value: 6,
            color: "#618d1b"
         },
         {
            label: "P",
            value: 22,
            color: "#1ee67b"
         },
         {
            label: "Q",
            value: 71,
            color: "#b0ec44"
         },
         {
            label: "R",
            value: 3,
            color: "#a4a0c9"
         },
         {
            label: "S",
            value: 5,
            color: "#322849"
         },
         {
            label: "T",
            value: 8,
            color: "#86f71a"
         },
         {
            label: "U",
            value: 1,
            color: "#d1c87f"
         },
         {
            label: "V",
            value: 1,
            color: "#7d9058"
         },
         {
            label: "X",
            value: 1,
            color: "#7c37c0"
         },
         {
            label: "Z",
            value: 2,
            color: "#efefef"
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
        <div className="container pt-5 mt-5">
        <ReactD3PieChart data={this.state.data} tooltip renderLabel={this.renderLabel} />
        </div>
    );
  }

}

export default PieChart;
