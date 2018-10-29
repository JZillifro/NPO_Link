import React from 'react';
import {Row, Col} from 'reactstrap';
import {Card, CardBody, CardText, CardTitle, Button, CardHeader} from 'reactstrap'
import {BASE_API_URL} from './../constants.jsx'
import axios from 'axios';
import RelatedModelList from './../RelatedModelList'

export default class NonprofitPage extends React.Component {

   constructor(props) {
     super(props);
     this.state = {
      nonprofit: {}
     };
   }

   componentDidMount() {
      axios.get(`${BASE_API_URL}/v1.0/nonprofits/nonprofit/${this.props.match.params.id}`).then(res => {
        const nonprofit = res.data.data.nonprofit;
        this.setState({nonprofit});
      }).catch(err => {
        console.log(err)
      });
   };

  render() {
    return (
      <div className="wrapper style1"  style={{background: "#fff", color: "rgb(43, 37, 44)", marginRight:"3%", marginLeft:"3%"}}>
        <Row  className="row">
         <Col xs={8} md={8} lg={8} className="pb-4">
            <Row className="row">
               <div className="col">
                 <div className="containter special" style={{textAlign: "center", marginRight:"5%", marginLeft:"5%"}}>
                   {/* <img src={this.state.nonprofit.image} alt={this.state.nonprofit.name} className="img-fluid" /> */}
                   <a className="image featured"><img src={this.state.nonprofit.logo} alt=""/></a>
                   <header>
                     <h2>{this.state.nonprofit.name}</h2>
                     <br/>
                     <p>{this.state.nonprofit.description}</p>
                     <a href="/categories" class="button">Back</a>
                   </header>
                 </div>
               </div>
            </Row>
         </Col>
         <Col xs={4} md={4} lg={4}  className="pb-4">
            <Row className="row justify-content-center">
                  <Col xs={12}>
                      <article className="">
                        <RelatedModelList model={"categories"} property={"nonprofit"} value={this.props.match.params.id}/>
                      </article>
                  </Col>
                  <Col xs={12} className="pt-3">
                    <article className="">
                      <RelatedModelList model={"locations"} property={"nonprofit"} value={this.props.match.params.id}/>
                    </article>
                  </Col>
            </Row>
         </Col>
        </Row>
      </div>
    )
  }
}
