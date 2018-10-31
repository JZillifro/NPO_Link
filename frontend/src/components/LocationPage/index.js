import React from 'react';
import {Row, Col} from 'reactstrap';
import {BASE_API_URL} from './../constants.jsx'
import axios from 'axios';
import RelatedModelList from './../RelatedModelList'
import GoogleMapReact from 'google-map-react';
import {getLocation} from './../../api/LocationAPI'

export default class locationPage extends React.Component {

   constructor(props) {
     super(props);
     this.state = {
      location: {},
      coords: {
        lat: 59.95,
        lng: 30.33
      }
     };
   }

   async componentDidMount() {
    const response = await getLocation(this.props.match.params.id);
    this.setState({location: response.data.data.category});
        };

  render() {
    return (
      <div className="wrapper style1"  style={{background: "#fff", color: "rgb(43, 37, 44)", marginRight:"3%", marginLeft:"3%"}}>
        <Row  className="row">
         <Col xs={8} md={8} lg={8} className="pb-4">
            <Row className="row">
               <div className="col">
                 <div className="containter special" style={{textAlign: "center", marginRight:"5%", marginLeft:"5%"}}>
                   {/* <img src={this.state.location.image} alt={this.state.location.name} className="img-fluid" /> */}
                   <a className="image featured"><img src={this.state.location.image} alt=""/></a>
                   <header>
                     <h2>{this.state.location.name}</h2>
                     <br/>
                     <p>{this.state.location.description}</p>
                     <a href="/categories" className="button">Back</a>
                   </header>
                 </div>
               </div>
            </Row>
         </Col>
         <Col xs={4} md={4} lg={4}  className="pb-4">
            <Row className="row justify-content-center">
                  <Col xs={12}>
                      <article className="">
                        <RelatedModelList model={"categories"} property={"location"} value={this.props.match.params.id} value2={"category"}/>
                      </article>
                  </Col>
                  <Col xs={12} className="pt-3">
                    <article className="">
                      <RelatedModelList model={"nonprofits"} property={"location"} value={this.props.match.params.id} value2={"nonprofit"}/>
                    </article>
                  </Col>
                  <Col xs={12} className="pt-3">
                    <div style={{ height: '400px', width: '400px' }}>
                      <GoogleMapReact
                        bootstrapURLKeys={{ key: "AIzaSyDfi87OPz0rr6f1oIQ_iH3boI4H53zLFAg"}}
                        defaultCenter={this.state.coords}
                        defaultZoom={11}>
                      </GoogleMapReact>
                    </div>
                  </Col>
            </Row>
         </Col>
        </Row>
      </div>
    )
  }
}
