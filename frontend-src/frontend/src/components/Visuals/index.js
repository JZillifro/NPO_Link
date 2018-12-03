import React, { Component } from 'react';
import HeatMap from './HeatMap'
import PieChart from './PieChart'
import BarChart from './BarChart'

class Visuals extends Component {

  render() {
    return (
        <div className="container pt-5 mt-5">
         <div className="row pt-5">
            <div className="container text-center">
            <h1>Heat Map of Nonprofits per State</h1>
            </div>
         </div>
         <div className="row">
         <HeatMap/>
         </div>
         <div className="row pt-5">
            <div className="container text-center">
            <h1>Breakdown of Nonprofits per Category</h1>
            </div>
         </div>
         <div className="row justify-content-center">
         <PieChart/>
         </div>
         <div className="row pt-5">
            <div className="container text-center">
            <h1>Breakdown of Volunteer Opportunities per State</h1>
            </div>
         </div>
         <div className="row mb-5">
         <BarChart/>
         </div>
        </div>
    );
  }

}

export default Visuals;
