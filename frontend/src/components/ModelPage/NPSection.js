import React from 'react';
import {PageHeader, Grid, Row, Col} from 'react-bootstrap';
import ModelPanel from './ModelPanel.js';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import axios from 'axios';
import {BASE_API_URL} from './../constants.jsx';
import { Pagination, PaginationItem, PaginationLink } from 'reactstrap';

export default class NPSection extends React.Component {
  constructor(props) {
    super(props)
    this.state = {}
  }

  componentDidMount() {
    axios.get(`${BASE_API_URL}/v1.0/${this.props.type}/1`).then(res => {
      const dataForPage = res.data.data.nonprofits
      console.log(dataForPage)
      const pages = res.data.pages

      this.setState({pages, dataForPage})
    }).catch(err => {
      console.log(err)
    });
  }

  changePage(i) {
    axios.get(`${BASE_API_URL}/v1.0/${this.props.type}/${i}`).then(res => {
      const dataForPage = res.data.data.nonprofits
      console.log(dataForPage)
      const pages = res.data.pages

      this.setState({pages, dataForPage})
    }).catch(err => {
      console.log(err)
    });
  }

  render() {
    // console.log("this.state.models")
    // console.log(this.state.models[this.props.type])
    var pagelinks = []
    for(var i = 1; i <= this.state.pages; i++) {
      const page = i;
      pagelinks.push(
        <PaginationItem>
          <PaginationLink onClick={() => this.changePage(page)}>
            {page}
          </PaginationLink>
        </PaginationItem>
      );
    }
    console.log(pagelinks)
    if(this.state.pages && this.state.dataForPage) {
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
          <Pagination aria-label="Page navigation example">
            {
              pagelinks.map((link) => {
                return(link)
              })
            }
          </Pagination>
        </div>
      );
    } else {
      return(<div></div>)
    }
  }
}
