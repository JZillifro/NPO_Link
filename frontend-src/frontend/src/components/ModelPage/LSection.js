import React from 'react';
import axios from 'axios';
import { BASE_API_URL, STATES } from './../constants.jsx';
import Pagination from "./../Pagination";
import { Card, CardBody, CardImg, CardText, Row, Col , CardHeader, Container} from 'reactstrap'
import SearchBar from './../SearchBar'
import DropdownChoices from './../Dropdown'
import Highlight from "react-highlighter";
import Image from "../../map.jpg"

export default class LSection extends React.Component {
   constructor(props) {
     super(props)
     this.state = {
       activePage: 1,
       dataForPage : [],
       query : '',
       dropdownOpen: false,
       sort_key: 'name',
       sort: 'asc',
       filters: {}
     }

     this.onChangePage = this.onChangePage.bind(this);
     this.onQueryChange = this.onQueryChange.bind(this);
     this.onSortChange = this.onSortChange.bind(this);
     this.resetPage = this.resetPage.bind(this);
     this.onStateChange = this.onStateChange.bind(this);
   }

   resetPage() {
      this.setState({
       activePage: 1,
       dataForPage : [],
       query : '',
       dropdownOpen: false,
       sort_key: 'id',
       sort: 'asc',
       filters: {}
     }, () => {
        this.refreshPage(1);
     })
   }

  componentWillMount() {
    console.log("");
     this.setState({activePage: 1}, () => {
        this.refreshPage(1);
     })
  }

  onChangePage(page) {
     this.setState({activePage: page}, () => {
         this.refreshPage(page);
     })
  }

  onQueryChange(query) {
     this.setState({query: query}, () => {
         this.refreshPage(1);
     })
  }

  onStateChange(state) {
    var filters = this.state.filters;
    filters['State'] = state;
     this.setState({filters}, () => {
         this.refreshPage(1);
     })
  }

  onSortChange(sort_key, sort) {
     console.log(sort)
     this.setState({sort_key: sort_key, sort: sort }, () => {
         this.refreshPage(1);
     })
  }

   refreshPage(page) {
      axios.get(`${BASE_API_URL}/v1.0/locations/search/${page}?search_words=${this.state.query}&sort=${this.state.sort}&filters=${JSON.stringify(this.state.filters)}&page_size=12`).then(res => {
        const dataForPage = res.data.data.locations
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

           <div class="wrapper style2">
             <article id="main" class="container special" style={{backgroundColor: "white"}}>
               <a href="#" class="image featured"><img src={Image} alt=""/></a>
             </article>
           </div>

            <Row className="mb-5">
               <Container className="justify-content-center">
                  <Row>
                   <Col xs={2}>
                      <h1>Filters:</h1>
                   </Col>
                   <DropdownChoices onClick={this.onStateChange}
                                    items={STATES}
                                    value={"State"}
                                    dropdownType={"state"}>
                   </DropdownChoices>
                  </Row>
               </Container>

               <SearchBar onSortChange={this.onSortChange} initialSortValue={'city'}
                          sort_keys={['city', 'state']}
                          onSearchChange={this.onQueryChange} initialSearchValue={'city'}
                          resetPage={this.resetPage} />
            </Row>

            <Row className="row justify-content-center">
              {
                this.state.dataForPage.map(model => (
                   <Col xs={12} sm={12} md={6} lg={4} className="pb-4 d-flex align-items-stretch" key={model.id}>
                      <Card>
                          <CardImg top width="100%"
                          href={"/location/" + model.id}
                          src={model.image}
                          className="card-img-top"
                          alt="Card image" />
                          <CardHeader style={{minHeight: "10vh"}}><a id={model.name} href={"/location/" + model.id} >{model.name}</a></CardHeader>
                          <CardBody className="block-with-text">
                             <CardText className="pt-2">
                               City:
                               <Highlight search={this.state.query}>{model.city}</Highlight>
                            </CardText>
                            <CardText className="pt-2">
                               State:
                               <Highlight search={this.state.query}>{model.state}</Highlight>
                            </CardText>
                            <CardText className="pt-2">
                               Description:
                               <Highlight search={this.state.query}>{model.description}</Highlight>
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
