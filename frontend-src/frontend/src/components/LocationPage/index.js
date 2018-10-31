import React from 'react';
import {Row, Col} from 'reactstrap';
import {BASE_API_URL} from './../constants.jsx'
import axios from 'axios';
import RelatedModelList from './../RelatedModelList'
import GoogleMapReact from 'google-map-react';
import LGMap from './LGMap.js'

export default class locationPage extends React.Component {

   constructor(props) {
     super(props);
     this.state = {
     };
   }

   componentDidMount() {
      axios.get(`${BASE_API_URL}/v1.0/locations/location/${this.props.match.params.id}`).then(res => {
        const location = res.data.data.location;
        this.setState({location});
      }).catch(err => {
        console.log(err)
      });
   };

  render() {
    if(this.state.location) {
      return (
        <div>
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
                         <a href="/Locations" className="button">Back</a>
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
                      <LGMap address={this.state.location.name} />
                </Row>
             </Col>
            </Row>
          </div>
        </div>
      )
    } else {
      return(<div></div>)
    }

  }
}
