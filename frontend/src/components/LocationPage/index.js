import React, { Component } from 'react'
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import { Row, Col, Card, CardBody, CardText, CardTitle, Button, CardHeader } from 'reactstrap'

class LocationPage extends Component {

   constructor(props) {
     super(props);
     this.state = {
      nonprofit: {},
      category: {},
      location: {}
     };
   }

   componentDidMount() {
      const location = LocationAPI.get(parseInt(this.props.match.params.id, 10))
      const category = CategoryAPI.get(parseInt(location.category, 10));
      const nonprofit = NonProfitAPI.get(parseInt(location.nonprofit, 10));

      this.setState({nonprofit, category, location});
   };

  render() {
    return (
      <div className="container">
       <Row  className="row">
         <Col xs={8} md={8} lg={8} className="pb-4">
            <Row className="row">
               <div className="col">
                  <img src={this.state.location.image} alt={this.state.location.name} className="img-fluid" />
               </div>
            </Row>
            <hr/>
            <Row className="row pt-5">
               <div className="col">
                  <h1>{this.state.location.name}</h1>
                  <br/>

                  <b>Description:</b><br/>
                  <p>{this.state.location.description}</p>
               </div>
            </Row>

         </Col>
         <Col xs={4} md={4} lg={4}  className="pb-4">
            <Row className="row justify-content-center">
                  <Col xs={12}>
                        <Card>
                          <CardHeader>Nonprofits</CardHeader>
                          <CardBody>
                            <CardTitle>{this.state.nonprofit.name}</CardTitle>
                            <CardText>{this.state.nonprofit.description}</CardText>
                            <Button href={"/nonprofit/" + this.state.nonprofit.id}> Learn more</Button>
                          </CardBody>
                        </Card>
                  </Col>
                  <Col xs={12} className="pt-3">
                        <Card>
                          <CardHeader>Categories</CardHeader>
                          <CardBody>
                            <CardTitle>{this.state.category.name}</CardTitle>
                            <CardText>{this.state.category.description}</CardText>
                            <Button href={"/category/" + this.state.category.id}> Learn more</Button>
                          </CardBody>
                        </Card>
                  </Col>
            </Row>
         </Col>
       </Row>
       <Button color="primary" href="/locations">Back</Button>
      </div>
    )
  }
}

export default LocationPage;
