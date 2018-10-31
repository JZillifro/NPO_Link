import React from 'react';
import {BASE_API_URL} from './../constants.jsx'
import axios from 'axios';

export default class RelatedModelList extends React.Component {

   constructor(props) {
     super(props);
     this.state = {};
   }

   componentDidMount() {
      if(this.props.property === 'nonprofit') {
         axios.get(`${BASE_API_URL}/v1.0/${this.props.model}/${this.props.property}/${this.props.value}`).then(res => {
           const model = res.data.data[this.props.value2];
           // console.log(res.json())
           this.setState({models : [model]});
         }).catch(err => {
           // console.log(err)
           this.setState({models : []});
         });
      } else {
         axios.get(`${BASE_API_URL}/v1.0/${this.props.model}/${this.props.property}/${this.props.value}`).then(res => {
           const models = res.data.data[this.props.model];
           // console.log(res.json())
           this.setState({models});
         }).catch(err => {
           // console.log(err)
           this.setState({models : []});
         });
      }

   };

  render() {
    if(this.state.models && this.state.models.length > 0){
      return (
        <div>
          <header>
            <h3><a>{this.props.model.charAt(0).toUpperCase() + this.props.model.slice(1)}</a></h3>
          </header>
          {
            this.state.models.map((model) => {
              return(
                <div key={model.id}>
                  <a href={"/" + this.props.value2 + "/" + model.id}>{model.name}</a>
                  <br/>
                </div>
              )
            })
          }
        </div>
      )
    } else {
      return (
         <div>
            <header>
               <h3><a>{this.props.model.charAt(0).toUpperCase() + this.props.model.slice(1)}</a></h3>
            </header>
            <div><p>No {this.props.model} found</p></div>
         </div>
      )
    }

  }
}
