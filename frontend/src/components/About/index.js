import React, { Component } from 'react'
import { Card, CardBody, CardImg, CardText, CardTitle, CardSubtitle, Row, Col } from 'reactstrap'

class About extends Component {
  constructor(props) {
    super(props);
    this.state = {
      contributors: []
    };
  }

  componentDidMount() {
    fetch('https://gitlab.com/api/v4/projects/8623652/repository/contributors')
    .then(response => response.json())
    .then(contributors => this.setState({contributors}))
  };

  render() {
    return (
        <div className="container">
           <Row className="row">
            {
              this.state.contributors.map(contributor => (
                 <Col xs={6} sm={6} md={4} lg={3} className="pb-4">
                    <Card key={contributor.email}>
                        <CardImg top width="100%"
                        src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180"
                        alt="Card image" />
                        <CardBody>
                          <CardTitle>{contributor.name}</CardTitle>
                          <CardSubtitle>{contributor.role}</CardSubtitle>
                          <CardText className="pt-2">
                             <p>
                             commits: {contributor.commits} <br/>
                             additions: {contributor.additions} <br/>
                             deletions: {contributor.deletions}
                             </p>
                          </CardText>
                        </CardBody>
                    </Card>
                 </Col>
              ))
            }
          </Row>
       </div>
    );
  }
}

export default About;
