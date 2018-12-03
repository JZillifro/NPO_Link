import React, { Component } from 'react';
import OtherPieChart from './OtherPieChart'
import Image from '../../diffChart.png';
import OtherHeatMap from './OtherHeatMap'

class ProviderVisuals extends Component {

  render() {
    return (
        <div className="container pt-5 mt-5 mb-5">
        <div className="row pt-5">
           <div className="container text-center">
           <h1>Number of Events per Month</h1>
           </div>
        </div>
         <div className="row">
         <OtherPieChart/>
         </div>
         <div className="row pt-5">
            <div className="container text-center">
            <h1>Poverty Difference Compared to Average</h1>
            </div>
         </div>
         <div className="row">
            <div className="containers">
               <img style={{maxWidth:"100%"}} src={Image} alt="Diff Chart"/>
            </div>
         </div>
         <div className="row pt-5">
            <div className="container text-center">
            <h1>Heat Map for Number of Events by Population for Each State</h1>
            </div>
         </div>
          <div className="row">
          <OtherHeatMap/>
          </div>
        </div>
    );
  }

}

export default ProviderVisuals;
