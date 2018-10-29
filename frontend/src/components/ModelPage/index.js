import React from 'react';
import {PageHeader, Grid, Row, Col} from 'react-bootstrap';
import ModelPanel from './ModelPanel.js';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import axios from 'axios';
import {BASE_API_URL} from './../constants.jsx';
import NPSection from './NPSection.js'

export default class ModelPage extends React.Component {
  constructor(props) {
    super(props)
    this.state = {}
  }

  render() {
    return(
      <div className="wrapper style1" style={{color: "rgb(43, 37, 44)"}}>

        <section id="features" className="container special">
          <header>
            <h2>{this.props.match.params.title}</h2>
            <p>Ipsum volutpat consectetur orci metus consequat imperdiet duis integer semper magna.</p>
          </header>
          <div className="row">
            {
              this.props.match.params.title == "nonprofits" && <NPSection type={this.props.match.params.title} />
            }
            {
              this.props.match.params.title == "categories" && <div>C</div>
            }
            {
              this.props.match.params.title == "locations" && <div>L</div>
            }
          </div>
        </section>

      </div>
    );
  }
}
