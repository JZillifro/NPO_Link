import React from 'react';
import {Row, Col} from 'reactstrap';
import {BASE_API_URL} from './../constants.jsx'
import axios from 'axios';
import RelatedModelList from './../RelatedModelList'
import GoogleMapReact from 'google-map-react';

export default class LGMap extends React.Component {

   constructor(props) {
     super(props);
     this.state = {
      coords: {
        lat: 59.95,
        lng: 30.33
      },
      'coordsLoading': true
     };
   }

   componentDidMount() {
     const addr = this.props.address.split(" ").join("+");
      axios.get(`https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDfi87OPz0rr6f1oIQ_iH3boI4H53zLFAg&address=${addr}`).then(res => {
        const location = res.data.results;
        console.log(location);
        this.setState({
          location: location[0],
          coords: {
            lat: location[0].geometry.location.lat,
            lng: location[0].geometry.location.lng
          },
          coordsLoading: false
        });
      }).catch(err => {
        console.log(err)
      });
   };

  render() {
    if(this.state.location){
      return (
        <Col xs={12} className="pt-3">
          <div style={{ height: '400px', width: '400px' }}>
            <GoogleMapReact
              bootstrapURLKeys={{ key: "AIzaSyDfi87OPz0rr6f1oIQ_iH3boI4H53zLFAg"}}
              defaultCenter={this.state.coords}
              defaultZoom={11}>
            </GoogleMapReact>
          </div>
        </Col>
      )
    } else {
      return (
        <Col xs={12} className="pt-3">
          
        </Col>
      )
    }

  }
}
