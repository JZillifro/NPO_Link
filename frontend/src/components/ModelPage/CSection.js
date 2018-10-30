import React from 'react';
import axios from 'axios';
import { BASE_API_URL } from './../constants.jsx';
import Pagination from "./../Pagination";
import { Card, CardBody, CardImg, CardText, Row, Col, CardHeader } from 'reactstrap'

export default class CSection extends React.Component {
   constructor(props) {
     super(props)
     this.state = {
      activePage: 1,
      dataForPage : []
     }
     this.onChangePage = this.onChangePage.bind(this);
   }

   componentWillMount() {
     axios.get(`${BASE_API_URL}/v1.0/categories/1`).then(res => {
       const dataForPage = res.data.data.categories
       const pages = res.data.pages
       this.setState({dataForPage: dataForPage, activePage: 1, totalPages: pages })
     }).catch(err => {
       console.log(err)
     });
   }

   onChangePage(page) {
      axios.get(`${BASE_API_URL}/v1.0/categories/${page}`).then(res => {
       const dataForPage = res.data.data.categories

       this.setState({activePage: page, dataForPage: dataForPage})
       window.scrollTo(0, 0)
      }).catch(err => {
       console.log(err)
      });
   }

  render() {
    if(this.state.dataForPage) {
      return(
         <div className="container justify-content-center">
             <Row className="row justify-content-center">
              {
                this.state.dataForPage.map(model => (
                   <Col xs={12} sm={12} md={6} lg={4} className="pb-4 d-flex align-items-stretch" key={model.id}>
                      <Card>
                          <CardImg top width="100%"
                          href={"/category/" + model.id}
                          src={model.image}
                          className="card-img-top"
                          alt="Card image" />
                          <CardHeader style={{minHeight: "10vh"}}><a href={"/category/" + model.id} >{model.name}</a></CardHeader>
                          <CardBody className="block-with-text">
                            <CardText className="pt-2">
                               Category Code: {model.code}
                            </CardText>
                            <CardText className="pt-2">
                               Parent Code: {model.parent_category}
                            </CardText>
                            <CardText className="pt-2">
                               Description: {model.description}
                            </CardText>
                          </CardBody>
                      </Card>
                   </Col>
                ))
              }
            </Row>
            <Row  className="pt-5 pb-1">
              <Pagination  initialPage={1} onChangePage={this.onChangePage} totalPages={this.state.totalPages} />
            </Row>

          </div>
      );
    } else {
      return(<div></div>)
    }
  }
}
