import React from 'react';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import {Row, Col} from 'reactstrap';
import {Card, CardBody, CardText, CardTitle, Button, CardHeader} from 'reactstrap'
import {BASE_API_URL} from './../constants.jsx'
import axios from 'axios';

export default class RelatedModelList extends React.Component {

   constructor(props) {
     super(props);
     this.state = {};
   }

   componentDidMount() {
      axios.get(`${BASE_API_URL}/v1.0/${this.props.model}/${this.props.property}/${this.props.value}`).then(res => {
        const models = res.data.data[this.props.model];
        console.log(models)
        this.setState({models});
      }).catch(err => {
        console.log(err)
      });
   };

  render() {
    if(this.state.models){
      return (
        <div>
          <header>
            <h3><a>{this.props.model}</a></h3>
          </header>
          {
            this.state.models.map((model) => {
              return(
                <div>
                  <a href={"/" + this.props.model + "/" + model.id}>{model.name}</a>
                  <br/>
                </div>
              )
            })
          }
        </div>
      )
    } else {
      return (<div></div>)
    }

  }
}
