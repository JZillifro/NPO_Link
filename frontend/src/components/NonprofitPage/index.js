import React from 'react';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import {Row, Col} from 'reactstrap';
import {Card, CardBody, CardText, CardTitle, Button, CardHeader} from 'reactstrap'

export default class NonprofitPage extends React.Component {
   constructor(props) {
     super(props);
     this.state = {
      nonprofit: {},
      location: {},
      category: {}
     };
   }

   componentDidMount() {
      const nonprofit = NonProfitAPI.get(parseInt(this.props.match.params.id, 10));
      const location = LocationAPI.get(parseInt(nonprofit.location, 10));
      const category = CategoryAPI.get(parseInt(nonprofit.category, 10));
      this.setState({nonprofit, location, category});
   };

  render() {
    return (
      <div className="container">
        <Row  className="row">
         <Col xs={8} md={8} lg={8} className="pb-4">
            <Row className="row">
               <div className="col">
                  <img src={this.state.nonprofit.image} alt={this.state.nonprofit.name} className="img-fluid" />
               </div>
            </Row>
            <hr/>
            <Row className="row pt-5">
               <div className="col">
                  <h1>{this.state.nonprofit.name}</h1>
                  <br/>

                  <b>Description:</b><br/>
                  <p>{this.state.nonprofit.description}</p>
               </div>
            </Row>

         </Col>
         <Col xs={4} md={4} lg={4}  className="pb-4">
            <Row className="row justify-content-center">
                  <Col xs={12}>
                        <Card>
                          <CardHeader>Location</CardHeader>
                          <CardBody>
                            <CardTitle>{this.state.location.name}</CardTitle>
                            <CardText>{this.state.location.description}</CardText>
                            <Button href={"/location/" + this.state.location.id}> Learn more</Button>
                          </CardBody>
                        </Card>
                  </Col>
                  <Col xs={12} className="pt-3">
                        <Card>
                          <CardHeader>Category</CardHeader>
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
        <Button color="primary" href="/nonprofits">Back</Button>
      </div>
    )
  }
}
