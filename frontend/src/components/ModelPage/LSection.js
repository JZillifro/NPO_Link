import React from 'react';
import {PageHeader, Grid, Row, Col} from 'react-bootstrap';
import ModelPanel from './ModelPanel.js';
import axios from 'axios';
import { BASE_API_URL } from './../constants.jsx';
import Pagination from "./../Pagination";

export default class LSection extends React.Component {
   constructor(props) {
     super(props)
     this.state = {
       activePage: 1,
       dataForPage : []
     }
     this.onChangePage = this.onChangePage.bind(this);
   }

  componentWillMount() {
    axios.get(`${BASE_API_URL}/v1.0/locations/1`).then(res => {
      const dataForPage = res.data.data.locations
      const pages = res.data.pages
      this.setState({dataForPage: dataForPage, activePage: 1, totalPages: pages })
    }).catch(err => {
      console.log(err)
    });
  }

  onChangePage(page) {
     axios.get(`${BASE_API_URL}/v1.0/locations/${page}`).then(res => {
      const dataForPage = res.data.data.locations

      this.setState({activePage: page, dataForPage: dataForPage})
      window.scrollTo(0, 0)
     }).catch(err => {
      console.log(err)
     });
  }

  render() {
    if(this.state.pages && this.state.dataForPage) {
      return(
        <div className="container justify-content-center">
          <div className="row">
            {
              this.state.dataForPage.map((model, i) => {
                return(
                  <article className="col-4 col-12-mobile special" style={{maxWidth: "30%"}}>
                    <a href={"/location/" + model.id} className="image featured"><img src={model.image} alt="" height="250" /></a>
                    <header>
                      <h3><a href="#">{model.name}</a></h3>
                    </header>
                    <p>
                      {model.description}
                    </p>
                    <p>
                      EIN: {model.ein}
                    </p>
                    <p>
                      Address: {model.address}
                    </p>
                  </article>
                )
              })
            }
          </div>
          <hr/>
          <Pagination  initialPage={1} onChangePage={this.onChangePage} totalPages={this.state.totalPages} />
        </div>
      );
    } else {
      return(<div></div>)
    }
  }
}
