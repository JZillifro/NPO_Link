import React, {Component} from 'react';
import * as d3 from 'd3';
import { ALL_STATES, STATE_PATHS, BASE_API_URL, STATES, OTHER_STATE_DATA, ABBREVIATIONS, FULL_NAME } from './../constants.jsx';
import axios from 'axios';

class OtherHeatMap extends Component {
   constructor(props) {
     super(props)
     this.state = {
     }
   }

   componentDidMount() {
      var org_data = {};

      ALL_STATES.forEach(state => org_data[state] = 0);

      for(var state in FULL_NAME) {
         org_data[ABBREVIATIONS[FULL_NAME[state]]] = OTHER_STATE_DATA[FULL_NAME[state]];
      }

      var sampleData ={};
      ALL_STATES.forEach(function(d){
            var count= org_data[d] * 10000;
            sampleData[d]= {count:count, color:d3.interpolate("#ffffcc", "#800026")(count/1)};
        });

      this.draw("#statesvg", sampleData);
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

export default OtherHeatMap;
