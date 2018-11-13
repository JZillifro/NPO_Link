import React from 'react';
import {Row, Col} from 'reactstrap';
import RelatedModelList from './../RelatedModelList'
import {getCategory} from './../../api/CategoryAPI'

export default class CategoryPage extends React.Component {

   constructor(props) {
     super(props);
     this.state = {
      category: {}
     };
   }

   async componentDidMount() {
     const response = await getCategory(this.props.match.params.id);
     this.setState({category: response.data.data.category});
   };

  render() {
    return (
      <div className="wrapper style1"  style={{background: "#fff", color: "rgb(43, 37, 44)", marginRight:"3%", marginLeft:"3%"}}>
        <Row  className="row">
         <Col xs={8} md={8} lg={8} className="pb-4">
            <Row className="row">
               <div className="col">
                 <div className="containter special" style={{textAlign: "center", marginRight:"5%", marginLeft:"5%"}}>
                   <a className="image featured"><img src={this.state.category.image} alt=""/></a>
                   <header>
                     <h2>{this.state.category.name}</h2>
                     <br/>
                     <p>{this.state.category.description}</p>
                     <a href="/Categories" className="button">Back</a>
                   </header>
                 </div>
               </div>
            </Row>
         </Col>
         <Col xs={4} md={4} lg={4}  className="pb-4">
            <Row className="row justify-content-center">
                  <Col xs={12}>
                      <article className="">
                        <RelatedModelList model={"nonprofits"} property={"category"}
                                          value={this.props.match.params.id} value2={"nonprofit"}/>
                      </article>
                  </Col>
                  <Col xs={12} className="pt-3">
                    <article className="">
                      <RelatedModelList model={"locations"} property={"category"}
                                        value={this.props.match.params.id} value2={"location"}/>
                    </article>
                  </Col>
            </Row>
         </Col>
        </Row>
      </div>
    )
  }
}
