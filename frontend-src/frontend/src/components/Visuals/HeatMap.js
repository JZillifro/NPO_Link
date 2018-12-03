import React, {Component} from 'react';
import * as d3 from 'd3';
import { ALL_STATES, STATE_PATHS, BASE_API_URL, STATES } from './../constants.jsx';
import axios from 'axios';

class HeatMap extends Component {
   constructor(props) {
     super(props)
     this.state = {
     }
   }

   componentDidMount() {
      axios.get(`${BASE_API_URL}/v1.0/locations/all`).then(res => {
         var locations = {};
         STATES.forEach(state => locations[state] = []);
         const data = res.data.data.locations;
         data.forEach(loc => locations[loc.state].push(loc.id));

         this.setState({locations: locations, data: data}, () => {
            const states = this.state.locations;
            var org_data = {};

            ALL_STATES.forEach(state => org_data[state] = 0);
            for(var state in states) {
               org_data[state] = this.state.data.filter(loc => states[state].indexOf(loc.id) > -1)
               .map(loc => loc.nonprofits.length)
               .reduce((acc, val) => acc + val, 0);
            }

            var sampleData ={};
            ALL_STATES.forEach(function(d){
                  var count= org_data[d];
                  sampleData[d]= {count:count, color:d3.interpolate("#ffffcc", "#800026")(count/23)};
              });
            this.draw("#statesvg", sampleData);
        })
     });

   }

   draw(id, data) {
      d3.select(id).selectAll(".state")
         .data(STATE_PATHS).enter().append("path").attr("class","state").attr("d",function(d){ return d.d;})
         .style("fill",function(d){return data[d.id].color; });
   }

  render(){
    return (<div className="container justify-content-center"><svg width="1260" height="900" id="statesvg"></svg></div>);
  }
}

export default HeatMap;
