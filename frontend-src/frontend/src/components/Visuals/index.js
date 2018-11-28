import React, { Component } from 'react';
import HeatMap from './HeatMap'
import PieChart from './PieChart'
import BarChart from './BarChart'

class Visuals extends Component {

  render() {
    return (
        <div className="container pt-5 mt-5">
         <div className="row">
         <HeatMap/>
         </div>
         <div className="row">
         <PieChart/>
         </div>
         <div className="row">
         <BarChart/>
         </div>
        </div>
    );
  }

}

export default Visuals;
