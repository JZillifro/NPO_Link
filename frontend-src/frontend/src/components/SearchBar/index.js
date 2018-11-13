import React, { Component } from 'react'
import {Col, Row, Container, Button} from 'reactstrap'
import PropTypes from 'prop-types'
import DropdownChoices from './../Dropdown'

const propTypes = {
    sort_keys: PropTypes.array.isRequired,
    initialSortValue: PropTypes.string.isRequired,
    initialSearchValue: PropTypes.string.isRequired,
    onSearchChange: PropTypes.func.isRequired,
    onSortChange: PropTypes.func.isRequired,
    resetPage: PropTypes.func.isRequired
}

class SearchBar extends Component {

  constructor(props) {
    super(props)
    this.state = {
      query: ''
    }

    this.onSortChange = this.onSortChange.bind(this);
    this.onSearchChange = this.onSearchChange.bind(this);
    this.onSortKeyChange = this.onSortKeyChange.bind(this);
    this.onSortValueChange = this.onSortValueChange.bind(this);
    this.resetPage = this.resetPage.bind(this);
  }

  onSortChange = (sort_key, sort) => {
     this.setState({
       sort_key: sort_key,
       sort: sort
     }, () => {
         this.props.onSortChange(this.state.sort_key, this.state.sort);
     })
  }

  onSearchChange = (query) => {
     this.setState({
       query: query
     }, () => {
         this.props.onSearchChange(this.state.query);
     })
  }

  onSortKeyChange = (sort_key) => {
     this.setState({
       sort_key: sort_key
     }, () => {
         this.props.onSortChange(this.state.sort_key, this.state.sort);
     })
  }

  onSortValueChange = (sort) => {
     this.setState({
       sort: sort
     }, () => {
         this.props.onSortChange(this.state.sort_key, this.state.sort);
     })
  }

  handleInputChange = () => {
    this.setState({
      query: this.search.value
    }, () => {
      if (this.state.query && this.state.query.length > 0) {
         this.props.onSearchChange(this.state.query);
      }
      else {
         this.props.onSearchChange('');
      }
    })
  }

  resetPage = () => {
     this.props.resetPage();
 }

  render() {
    return (
      <Container className="mb-5 justify-content-center">
         <Row className="mb-5">
            <Col xs={2}>
            </Col>
            <Col xs={2}>
               <Button onClick={this.resetPage}>Reset</Button>
            </Col>
            <Col xs={3}>
               <form id="search_bar" className="form-inline">
                <input className="form-control mr-md-2" type="search" placeholder="Search..." aria-label="Search"
                        ref={input => this.search = input} onChange={this.handleInputChange}/>
               </form>
            </Col>
            <Col xs={1}>
               <DropdownChoices onClick={this.onSortKeyChange}
                                items={this.props.sort_keys}
                                value={this.props.initialSortValue}>
               </DropdownChoices>
            </Col>
            <Col xs={1}>
               <DropdownChoices onClick={this.onSortValueChange}
                                items={['asc', 'desc']}
                                value={'asc'}>
               </DropdownChoices>
            </Col>
         </Row>
      </Container>
    )
  }
}

SearchBar.propTypes = propTypes;
export default SearchBar
