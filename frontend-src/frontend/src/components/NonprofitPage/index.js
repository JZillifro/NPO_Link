import React from 'react';
import {Row, Col} from 'reactstrap';
import RelatedModelList from './../RelatedModelList'
import {getNonProfit} from './../../api/NonProfitAPI'

export default class NonprofitPage extends React.Component {

   constructor(props) {
     super(props);
     this.state = {};
   }

   async componentDidMount() {
    const response = await getNonProfit(this.props.match.params.id);
    this.setState({nonprofit: response.data.data.nonprofit});
        };

  render() {
    if(this.state.nonprofit){
      return (
        <div className="wrapper style1"  style={{background: "#fff", color: "rgb(43, 37, 44)", marginRight:"3%", marginLeft:"3%"}}>
          <Row  className="row">
           <Col xs={8} md={8} lg={8} className="pb-4">
              <Row className="row">
                 <div className="col">
                   <div className="containter special" style={{textAlign: "center", marginRight:"5%", marginLeft:"5%"}}>
                     <a className="image featured"><img src={this.state.nonprofit.logo} alt=""/></a>
                     <header>
                       <h2>{this.state.nonprofit.name}</h2>
                       <br/>
                       <p>{this.state.nonprofit.description}</p>
                       <a href="/Nonprofits" className="button">Back</a>
                     </header>
                   </div>
                 </div>
              </Row>
           </Col>
           <Col xs={4} md={4} lg={4}  className="pb-4">
              <Row className="row justify-content-center">
                    <Col xs={12}>
                        <article className="">
                          <RelatedModelList model={"categories"} property={"nonprofit"}
                             value={this.props.match.params.id} value2={"category"}
                             value3={this.state.nonprofit.category_id} />
                        </article>
                    </Col>
                    <Col xs={12} className="pt-3">
                      <article className="">
                        <RelatedModelList model={"locations"} model2={"location"} property={"nonprofit"}
                             value={this.props.match.params.id} value2={"location"}
                             value3={this.state.nonprofit.location_id} />
                      </article>
                    </Col>
                    <Col xs={12}>
                      <article className="">
                      <header>
                        <h3><a>Events</a></h3>
                        {
                          this.state.nonprofit.projects.map((project) => {
                            return(
                              <div><a href={project.projectLink}>{project.title}</a><br/></div>
                            )
                          })
                        }
                      </header>
                      </article>
                    </Col>
              </Row>
           </Col>
          </Row>
        </div>
      )
    } else {
      return(
        <div></div>
      )
    }

  }
}
