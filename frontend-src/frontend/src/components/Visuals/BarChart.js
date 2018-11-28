import React, {Component} from 'react';
import * as d3 from 'd3';
import axios from 'axios';
import { BASE_API_URL, STATES } from './../constants.jsx';

class BarChart extends Component {
   constructor(props) {
     super(props)
     this.state = {
     }
   }

   componentDidMount() {

      axios.get(`${BASE_API_URL}/v1.0/locations/all`).then(res => {
         var locations = {};
         STATES.forEach(state => locations[state] = []);
         res.data.data.locations.forEach(loc => locations[loc.state].push(loc.id));

         this.setState({locations: locations}, () => {
            axios.get(`${BASE_API_URL}/v1.0/nonprofits/all`).then(res => {
             var data = res.data.data.nonprofits;
             const org_data = [];
             const states = this.state.locations;
             for(var state in states) {
               var value = {}

               value.count = data.filter(org => states[state].indexOf(org.location_id) > -1)
               .map(org => org.projects.length)
               .reduce((acc, val) => acc + val, 0);

               value.state = state;

               org_data.push(value);
             }
             this.drawChart(org_data);
           });
        })
     });
   }

  drawChart(data) {
    //const data = [12, 5, 6, 6, 9, 10];
    const w = 1000;
    const h = 1000;

    const svg = d3.select("#container")
    .append("svg")
    .attr("width", w)
    .attr("height", h)

    svg.selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", (d, i) => i * 25)
      .attr("y", (d, i) => h - 10 * (d.count / 2))
      .attr("width", 20)
      .attr("height", (d, i) => d.count * 10)
      .attr("fill", "green")

     svg.selectAll("text")
      .data(data)
      .enter()
      .append("text")
      .text((d) => d.state)
      .attr("x", (d, i) => i * 25)
      .attr("y", (d, i) => h - ((10 * d.count) / 2) - 3)
  }

  render(){
    return (<div className="container mt-5 mb-5" id="container"></div>);
  }
}

export default BarChart;
