import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import { BASE_API_URL } from './../constants.jsx';
import Pagination from "./../Pagination";
import { Card, CardBody, CardImg, CardText, Row, Col, CardHeader } from 'reactstrap'

const propTypes = {
    query: PropTypes.string.isRequired
}

class NPSection extends React.Component {
   constructor(props) {
     super(props)
     this.state = {
      activePage: 1,
      dataForPage : [],
      query : '',
     }

     this.onChangePage = this.onChangePage.bind(this);
   }

   componentWillReceiveProps(props){
     const {query} = this.props
     if (props.query !== query) {
        this.setState({ query: props.query }, () => {
          this.refreshPage(1);
       })
     }
   }

   componentWillMount() {
      this.setState({activePage: 1}, () => {
         this.refreshPage(1);
      })
   }

   onChangePage(page) {
      this.setState({activePage: page}, () => {
          this.refreshPage(page);
      })
   }

   refreshPage(page) {
      axios.get(`${BASE_API_URL}/v1.0/nonprofits/search/${page}?search_words=${this.state.query}`).then(res => {
        console.log(res)
        const dataForPage = res.data.data.nonprofits
        const pages = res.data.pages
        this.setState({dataForPage: dataForPage, activePage: page, totalPages: pages })
      }).catch(err => {
        console.log(err)
      });
   }

  render() {
     if(this.state.dataForPage && this.state.dataForPage.length > 0) {
       return(
       <div className="container justify-content-center mt-5 mb-5">
           <Row className="row justify-content-center">
              <h1>Results for Nonprofits:</h1>
           </Row>
           <Row className="row justify-content-center">
             {
               this.state.dataForPage.map(model => (
                  <Col xs={12} sm={12} md={6} lg={4} className="pb-4 d-flex align-items-stretch" key={model.id}>
                     <Card>
                         <CardImg top width="100%"
                         href={"/nonprofit/" + model.id}
                         src={model.logo}
                         className="card-img-top"
                         alt="Card image" />
                         <CardHeader style={{minHeight: "10vh"}}><a href={"/nonprofit/" + model.id} >{model.name}</a></CardHeader>
                         <CardBody className="block-with-text">
                           <CardText className="pt-2">
                             Address: {model.address}
                           </CardText>
                           <CardText className="pt-2">
                             EIN: {model.ein}
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
        return(
           <div className="container justify-content-center mt-5 mb-5">
              <Row className="row justify-content-center">
              <h1>No Results Found for Nonprofits</h1>
              </Row>
           </div>
        )
     }
  }
}

NPSection.propTypes = propTypes;
export default NPSection;
