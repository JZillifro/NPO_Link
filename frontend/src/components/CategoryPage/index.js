import React from 'react';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';
import {Row, Col} from 'reactstrap';
import {Card, CardBody, CardText, CardTitle, Button, CardHeader} from 'reactstrap'
import {BASE_API_URL} from './../constants.jsx'
import axios from 'axios';
import RelatedModelList from './../RelatedModelList'

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
      axios.get(`${BASE_API_URL}/v1.0/categories/category/${this.props.match.params.id}`).then(res => {
        const category = res.data.data.category;
        this.setState({category});
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
                   {/* <img src={this.state.category.image} alt={this.state.category.name} className="img-fluid" /> */}
                   <a className="image featured"><img src={this.state.category.image} alt=""/></a>
                   <header>
                     <h2>{this.state.category.name}</h2>
                     <br/>
                     <p>{this.state.category.description}</p>
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
                        <header>
                          <h3><a>Nonprofits</a></h3>
                        </header>
                        <RelatedModelList model={"nonprofits"} property={"category"} value={this.props.match.params.id}/>
                      </article>
                  </Col>
                  <Col xs={12} className="pt-3">
                    <article className="">
                      <header>
                        <h3><a>Locations</a></h3>
                      </header>
                      <RelatedModelList model={"locations"} property={"category"} value={this.props.match.params.id}/>
                    </article>
                  </Col>
            </Row>
         </Col>
        </Row>
      </div>
    )
  }
}
