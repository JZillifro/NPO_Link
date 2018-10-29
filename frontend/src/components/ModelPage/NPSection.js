import React from 'react';
import ReactDOM from "react-dom";
import {PageHeader, Grid, Row, Col} from 'react-bootstrap';
import ModelPanel from './ModelPanel.js';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import axios from 'axios';
import { BASE_API_URL } from './../constants.jsx';

import Pagination from "react-js-pagination";

export default class NPSection extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      activePage: 1,
      dataForPage : [],
      totalNum: 12
    }
  }

  componentDidMount() {
    axios.get(`${BASE_API_URL}/v1.0/${this.props.type}/1`).then(res => {
      const dataForPage = res.data.data.nonprofits

      this.setState({dataForPage: dataForPage, activePage: 1})
    }).catch(err => {
      console.log(err)
    });
  }

  changePage(i) {
       axios.get(`${BASE_API_URL}/v1.0/${this.props.type}/${i}`).then(res => {
         const dataForPage = res.data.data.nonprofits

         this.setState({activePage: i, dataForPage: dataForPage})
         window.scrollTo(0, 0)
       }).catch(err => {
         console.log(err)
       });
  }

  render() {
    if(this.state.dataForPage) {
      return(
        <div>
          <div className="row">
            {
              this.state.dataForPage.map((model, i) => {
                return(
                  <article className="col-4 col-12-mobile special">
                    <a href={"/nonprofit/" + model.id} className="image featured"><img src={model.logo} alt="" height="250"/></a>
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
          <br/>

          <Pagination pageRangeDisplayed={10} activePage={this.state.activePage}
                      activeLinkClass = "active" totalItemsCount={this.state.totalNum}
                      itemsCountPerPage={12}
                      onChange={this.changePage} />

        </div>
      );
    } else {
      return(<div></div>)
    }
  }
}
