import React, { Component } from 'react';
import { Col, Row } from 'reactstrap';

class AppFooter extends Component {
  render() {
    return (
      <div id="footer">
        <hr/>
        <Row>
          <Col>
              <section className="contact">
                <p>cs373 10 AM Group 6 2018</p>
              </section>
              <div className="copyright">
                <ul className="menu">
                  <li>&copy; NPOLink</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                </ul>
              </div>

          </Col>

        </Row>
      </div>
    );
  }
}

export default AppFooter;
