import React, { Component } from 'react';
import { Col, Row } from 'reactstrap';

class AppFooter extends Component {
  render() {
    return (
      <footer>
         <hr />
         <Row>
            <Col xs={12}>
               <p>© cs373 10 AM Group 6 2018</p>
            </Col>
         </Row>
      </footer>
    );
  }
}

export default AppFooter;
