import React from 'react';
import {PageHeader, Grid, Row, Col} from 'react-bootstrap';
import ModelPanel from './ModelPanel.js';
import NonProfitAPI from './../../api/NonProfitAPI';
import LocationAPI from './../../api/LocationAPI';
import CategoryAPI from './../../api/CategoryAPI';

export default class ModelPage extends React.Component {
  render() {
      if(this.props.match.params.title === "nonprofits"){
        return(<div className="container">
          <PageHeader style={{backgroundColor: "#b4eeb4"}}>
            <div style={{marginLeft: "20px"}}>
              <br/>
              <h1>Non-Profit Organizations</h1>
              <div><small>Nonprofit organizations are accountable to the donors, funders, volunteers, program recipients, and the public community.</small></div>
              <br/>
            </div>
          </PageHeader>

          <Grid>
            <Row>
               {
                NonProfitAPI.all().map(nonprofit => (
                    <Col xs={6} md={4}>
                      <ModelPanel
                        title = {nonprofit.name}
                        description = {nonprofit.description}
                        image = {nonprofit.image} alt="242x200"
                        id = {nonprofit.id}
                        type = "nonprofit"
                      />
                    </Col>
                ))
               }
            </Row>
          </Grid>
        </div>);
     } else if(this.props.match.params.title === "locations"){
        return(<div className="container">
          <PageHeader style={{backgroundColor: "#b4eeb4"}}>
            <div style={{marginLeft: "20px"}}>
              <br/>
              <h1>Locations</h1>
              <div><small>These are various cities which have nonprofit organizations.</small></div>
              <br/>
            </div>
          </PageHeader>


          <Grid>
            <Row>
            {
             LocationAPI.all().map(location => (
                 <Col xs={6} md={4}>
                   <ModelPanel
                     title = {location.name}
                     description = {location.description}
                     image = {location.image} alt="242x200"
                     id = {location.id}
                     type = "location"
                   />
                 </Col>
             ))
            }
            </Row>
          </Grid>
        </div>);
     } else if(this.props.match.params.title === "categories"){
        return(<div className="container">
          <PageHeader style={{backgroundColor: "#b4eeb4"}}>
            <div style={{marginLeft: "20px"}}>
              <br/>
              <h1>Categories</h1>
              <div><small>These are various types of nonprofit organizations.</small></div>
              <br/>
            </div>
          </PageHeader>

          <Grid>
            <Row>
            {
             CategoryAPI.all().map(category => (
                 <Col xs={6} md={4}>
                   <ModelPanel
                     title = {category.name}
                     description = {category.description}
                     image = {category.image} alt="242x200"
                     id = {category.id}
                     type = "category"
                   />
                 </Col>
             ))
            }
            </Row>
          </Grid>
        </div>);
      } else {
        return (<div>OUCH</div>)
      }
  }
}
