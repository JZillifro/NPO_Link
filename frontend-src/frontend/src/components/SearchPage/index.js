import React from 'react';
import {Col, Row, Container, Button} from 'reactstrap'
import CSection from './CSection';

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
                {this.state.query}
                 <form className="form-inline">
                  <input className="form-control mr-md-2" type="search" placeholder="Search..." aria-label="Search"
                          ref={input => this.search = input}/>
                 </form>
                 <button onClick={this.handleInputChange}>Submit</button>
              </Col>
           </Row>
        </Container>
        <CSection query={this.state.query}/>
      </div>
    )
  }
}
