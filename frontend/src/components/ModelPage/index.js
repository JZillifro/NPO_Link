import React from 'react';
import {PageHeader, Grid, Row, Col} from 'react-bootstrap';
import ModelPanel from './ModelPanel.js';

export default class ModelPage extends React.Component {
  render() {
      if(this.props.match.params.title == "nonprofits"){
        return(<div className="container">
          <PageHeader>
            <div>Non-Profit Organizations</div>
            <div><small>Nonprofit organizations are accountable to the donors, funders, volunteers, program recipients, and the public community.</small></div>
          </PageHeader>

          <Grid>
            <Row>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "Austin Film Festival"
                  description = "Austin Film Festival furthers the art and craft of storytelling by inspiring and championing the work of writers, filmmakers, and all artists who use written and visual language to tell a story."
                  image = "https://www.austinchronicle.com/binary/784a/austinfilmfestival-logo.jpg" alt="242x200"
                  id = "21"
                />
              </Col>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "CanCare"
                  description = "CanCare is a mighty community of survivors who lift up and inspire cancer patients and caregivers through one-on-one support, empathy, and hope."
                  image = "https://s.hdnux.com/photos/52/37/17/11137986/7/920x920.jpg" alt="242x200"
                  id = "22"
                />
              </Col>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "Soldier's Angels"
                  description = "Soldiers' Angels provides aid and comfort to the men and women of the United States Army, Marines, Navy, Air Force, Coast Guard, their families, and a growing veteran population."
                  image = "https://www.mrcy.com/contentassets/59c8f195f9c8409282b353a5fce7deb3/soldiers-and-angels-lrg.jpg" alt="242x200"
                  id = "23"
                />
              </Col>
            </Row>
          </Grid>
        </div>);
      } else if(this.props.match.params.title == "locations"){
        return(<div className="container">
          <PageHeader>
            <div>Locations</div>
            <div><small>These are various cities which have nonprofit organizations.</small></div>
          </PageHeader>

          <Grid>
            <Row>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "Austin, Texas"
                  description = "Austin is the state capital of Texas, an inland city bordering the Hill Country region."
                  image = "https://s.yimg.com/ny/api/res/1.2/F5QNZk6yFsCo.xljxX7Nwg--~A/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9ODAw/http://media.zenfs.com/en-US/homerun/businessinsider.com/686264f597202e8902e8ccbe53d74fc4" alt="242x200"
                  id = "24"
                />
              </Col>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "Houston, Texas"
                  description = "Houston is a large metropolis in Texas, extending to Galveston Bay."
                  image = "https://assets3.thrillist.com/v1/image/1808718/size/tmg-article_default_mobile.jpg" alt="242x200"
                  id = "25"
                />
              </Col>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "San Antonio, Texas"
                  description = "San Antonio is a major city in south-central Texas with a rich colonial heritage."
                  image = "https://www.tripsavvy.com/thmb/bN3MDpQtAZpnsP--SSVgqtVhNjg=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/downtown-san-antonio-180514061-598b9a4c396e5a00101781c1.jpg" alt="242x200"
                  id = "26"
                />
              </Col>
            </Row>
          </Grid>
        </div>);
      } else if(this.props.match.params.title == "categories"){
        return(<div className="container">
          <PageHeader>
            <div>Categories</div>
            <div><small>These are various types of nonprofit organizations.</small></div>
          </PageHeader>

          <Grid>
            <Row>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "Film/Video"
                  description = "These organization support independant film makers."
                  image = "https://3.imimg.com/data3/TS/GF/MY-3304941/ad-flim-making-services-250x250.jpg" alt="242x200"
                  id = "27"
                />
              </Col>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "Disease"
                  description = "These organizations support medical research."
                  image = "https://www.irishcentral.com/uploads/article/13911/cropped_Hemochromatosis_celtic_blood_disease_iStock.jpg?t=1516784551" alt="242x200"
                  id = "28"
                />
              </Col>
              <Col xs={6} md={4}>
                <ModelPanel
                  title = "Disaster Preparedness"
                  description = "These organization help prepare cities and their community for natural disasters"
                  image = "https://www.dominicavibes.dm/wp-content/uploads/2018/03/14297991.54854f3816f2f.jpg" alt="242x200"
                  id = "29"
                />
              </Col>
            </Row>
          </Grid>
        </div>);
      } else {
        return (<div>OUCH</div>)
      }
  }
}
