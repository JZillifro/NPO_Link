import React from 'react';
import {Col, Row, Container, Button} from 'reactstrap'
import CSection from './CSection';
import LSection from './LSection';
import NPSection from './NPSection';

export default class SearchPage extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      query: ""
    }
  }
  handleInputChange = () => {
    this.setState({
      query: this.search.value
    });
  }
  render() {
    return (
      <div>
        <Container className="mb-5 justify-content-center" style={{marginTop: "10%"}}>
           <Row className="mb-5">
              <Col xs={3}>
                 <form className="form-inline">
                  <input id="search_bar" className="form-control mr-md-2" type="search" placeholder="Search..." aria-label="Search"
                          ref={input => this.search = input}/>
                 </form>
              </Col>
              <Col>
               <Button id="submit_button" onClick={this.handleInputChange}>Submit</Button>
              </Col>
           </Row>
        </Container>
        <CSection query={this.state.query}/>
        <LSection query={this.state.query}/>
        <NPSection query={this.state.query}/>
      </div>
    )
  }
}
