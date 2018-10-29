import React, { Component } from 'react';
import { Col, Row } from 'reactstrap';

class AppFooter extends Component {
  render() {
    return (
      // <footer>
      //    <hr />
      //    <Row>
      //       <Col xs={12}>
      //          <p>© cs373 10 AM Group 6 2018</p>
      //       </Col>
      //    </Row>
      // </footer>
      <div id="footer">
        <hr/>
        <div className="row">
          <div className="col-12">
              <section className="contact">
                {/* <header>
                  <h3>© cs373 10 AM Group 6 2018</h3>
                </header> */}
                <p>cs373 10 AM Group 6 2018</p>
                {/* <ul className="icons">
                  <li><a href="#" className="icon fa-twitter"><span className="label">Twitter</span></a></li>
                  <li><a href="#" className="icon fa-facebook"><span className="label">Facebook</span></a></li>
                  <li><a href="#" className="icon fa-instagram"><span className="label">Instagram</span></a></li>
                  <li><a href="#" className="icon fa-pinterest"><span className="label">Pinterest</span></a></li>
                  <li><a href="#" className="icon fa-dribbble"><span className="label">Dribbble</span></a></li>
                  <li><a href="#" className="icon fa-linkedin"><span className="label">Linkedin</span></a></li>
                </ul> */}
              </section>
              <div className="copyright">
                <ul className="menu">
                  <li>&copy; NPOLink</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                </ul>
              </div>

          </div>

        </div>
      </div>
    );
  }
}

export default AppFooter;
