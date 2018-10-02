import React from 'react';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import {Row, Col} from 'reactstrap';
import {Card, CardBody, CardText, CardTitle, Button, CardHeader} from 'reactstrap'

export default class CategoryPage extends React.Component {

   constructor(props) {
     super(props);
     this.state = {
      nonprofit: {},
      category: {},
      location: {}
     };
   }

   componentDidMount() {
      const category = CategoryAPI.get(parseInt(this.props.match.params.id, 10));
      const nonprofit = NonProfitAPI.get(parseInt(category.nonprofit, 10));
      const location = LocationAPI.get(parseInt(category.location, 10))
      this.setState({nonprofit, category, location});
   };

  render() {
    return (
      <div className="container">
        <Row  className="row">
         <Col xs={8} md={8} lg={8} className="pb-4">
            <Row className="row">
               <div className="col">
                  <img src={this.state.category.image} alt={this.state.category.name} className="img-fluid" />
               </div>
            </Row>
            <hr/>
            <Row className="row pt-5">
               <div className="col">
                  <h1>{this.state.category.name}</h1>
                  <br/>

                  <b>Description:</b><br/>
                  <p>{this.state.category.description}</p>
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
                          <CardHeader>Locations</CardHeader>
                          <CardBody>
                            <CardTitle>{this.state.location.name}</CardTitle>
                            <CardText>{this.state.location.description}</CardText>
                            <Button href={"/location/" + this.state.location.id}> Learn more</Button>
                          </CardBody>
                        </Card>
                  </Col>
            </Row>
         </Col>
        </Row>
        <Button color="primary" href="/categories">Back</Button>
      </div>
    )
  }
}
