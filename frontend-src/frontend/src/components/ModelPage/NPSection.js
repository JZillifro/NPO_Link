import React from 'react';
import axios from 'axios';
import { BASE_API_URL, STATES } from './../constants.jsx';
import Pagination from "./../Pagination";
import { Card, CardBody, CardImg, CardText, Row, Col , CardHeader} from 'reactstrap'
import SearchBar from './../SearchBar'
import DropdownChoices from './../Dropdown'
import Highlight from "react-highlighter";
import Image from "../../hands2.jpg";

export default class NPSection extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
     activePage: 1,
     dataForPage : [],
     query : '',
     sort: 'asc',
     filters: {}
    }

    this.onChangePage = this.onChangePage.bind(this);
    this.onQueryChange = this.onQueryChange.bind(this);
    this.onSortChange = this.onSortChange.bind(this);
    this.onStateChange = this.onStateChange.bind(this);
    this.onRangeChange = this.onRangeChange.bind(this);
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

  onQueryChange(query) {
     this.setState({query: query}, () => {
         this.refreshPage(1);
     })
  }

  onSortChange(sort_key, sort) {
     console.log(sort)
     this.setState({sort_key: sort_key, sort: sort }, () => {
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

  onRangeChange(value) {
    var filters = this.state.filters;
    filters['Range'] = value;
     this.setState({filters}, () => {
         this.refreshPage(1);
     })
  }

  resetPage() {
     this.setState({
      activePage: 1,
      dataForPage : [],
      query : '',
      sort_key: 'id',
      sort: 'asc',
      filters: {}
    }, () => {
       this.refreshPage(1);
    })
  }

  refreshPage(page) {
     axios.get(`${BASE_API_URL}/v1.0/nonprofits/search/${page}?search_words=${this.state.query}&sort=${this.state.sort}&sort_key=${this.state.sort_key}&filters=${JSON.stringify(this.state.filters)}&page_size=12`).then(res => {
       const dataForPage = res.data.data.nonprofits
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
              <div className="image featured" style={{position:"relative", textAlign:"center"}}><img src={Image} alt="" className="card-img-top"/><h1 style={{position:"absolute", top:"50%", left:"50%", transform:"translate(-50%, -50%)", color:"white", fontSize:"1000%"}}>Nonprofits</h1></div>
              <header><h2>Nonprofit organizations are accountable to the donors, funders, volunteers, program recipients, and the public community.</h2></header>
            </article>
          </div>

          <Row className="mb-5">
              <Col xs={2}>
              <h1>Filters:</h1>
              </Col>
              <Col xs={2}>
                 <DropdownChoices onClick={this.onStateChange}
                                  items={STATES}
                                  value={"State"}
                                  dropdownType={"state"}>

                 </DropdownChoices>
              </Col>
              <Col xs={2}>
                 <DropdownChoices onClick={this.onRangeChange}
                                  items={[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}
                                  value={"Num. Events"}
                                  dropdownType={"num_projects"}>

                 </DropdownChoices>
              </Col>
             <SearchBar onSortChange={this.onSortChange} initialSortValue={'name'}
                        sort_keys={['name', 'ein']}
                        onSearchChange={this.onQueryChange} initialSearchValue={'name'}
                        resetPage={this.resetPage} />
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
                        <CardHeader style={{minHeight: "10vh"}}><a id={model.name} href={"/nonprofit/" + model.id} >{model.name}</a></CardHeader>
                        <CardBody className="block-with-text">
                          <CardText className="pt-2">
                             Address:
                             <Highlight search={this.state.query}> {model.address}</Highlight>
                          </CardText>
                          <CardText className="pt-2">
                             EIN:
                             <Highlight search={this.state.query}> {model.ein}</Highlight>
                          </CardText>
                          <CardText className="pt-2">
                             Description:
                             <Highlight search={this.state.query}> {model.description}</Highlight>
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
