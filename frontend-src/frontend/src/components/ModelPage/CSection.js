import React from 'react';
import axios from 'axios';
import { BASE_API_URL } from './../constants.jsx';
import Pagination from "./../Pagination";
import { Card, CardBody, CardImg, CardText, Row, Col, CardHeader } from 'reactstrap'
import SearchBar from './../SearchBar'

export default class CSection extends React.Component {
   constructor(props) {
     super(props)
     this.state = {
      activePage: 1,
      dataForPage : [],
      query : '',
      search_key: 'name',
      sort_key: 'name',
      sort: 'asc'
     }

     this.onChangePage = this.onChangePage.bind(this);
     this.onQueryChange = this.onQueryChange.bind(this);
     this.onSortChange = this.onSortChange.bind(this);
     this.resetPage = this.resetPage.bind(this);
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

   onQueryChange(search_key, query) {
      this.setState({query: query, search_key: search_key }, () => {
          this.refreshPage(1);
      })
   }

   onSortChange(sort_key, sort) {
      console.log(sort)
      this.setState({sort_key: sort_key, sort: sort }, () => {
          this.refreshPage(1);
      })
   }

   resetPage() {
      this.setState({
       activePage: 1,
       dataForPage : [],
       query : '',
       search_key: 'name',
       sort_key: 'id',
       sort: 'asc'
     }, () => {
        this.refreshPage(1);
     })
   }

   refreshPage(page) {
      axios.get(`${BASE_API_URL}/v1.0/categories/${page}?q=${this.state.query}&search_key=${this.state.search_key}&sort=${this.state.sort}&sort_key=${this.state.sort_key}`).then(res => {
        const dataForPage = res.data.data.categories
        const pages = res.data.pages
        this.setState({dataForPage: dataForPage, activePage: page, totalPages: pages })
        window.scrollTo(0, 0)
      }).catch(err => {
        console.log(err)
      });
   }

  render() {
    if(this.state.dataForPage) {
      return(
         <div className="container justify-content-center">
             <Row className="mb-5">
               <SearchBar onSortChange={this.onSortChange} initialSortValue={'name'}
                          sort_keys={['name', 'code']}
                          onSearchChange={this.onQueryChange} initialSearchValue={'name'}
                          search_keys={['name', 'code', 'parent', 'desc']}
                          resetPage={this.resetPage} />
             </Row>
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
