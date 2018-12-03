import React, { Component } from 'react';
import OtherPieChart from './OtherPieChart'
import Image from '../../diffChart.png';

class ProviderVisuals extends Component {

  render() {
    return (
        <div className="container pt-5 mt-5 mb-5">
         <div className="row">
         <OtherPieChart/>
         </div>
         <div className="row">
            <div classname="containers">
               <img style={{maxWidth:"100%"}} src={Image} alt="Diff Chart"/>
            </div>
         </div>
         <div className="row">
         </div>
        </div>
    );
  }

}

export default ProviderVisuals;
