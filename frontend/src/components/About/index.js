import React, { Component } from 'react'
import { Card, CardBody, CardImg, CardText, CardSubtitle, Row, Col , CardDeck, CardHeader, CardFooter} from 'reactstrap'

const avatar = require("./../../avatar.png")

class About extends Component {
  constructor(props) {
    super(props);
    this.state = {
      contributors: [
         {name: "Georgina Garza", gitlab_name: "Georgina Garza", role: "Developer", image: avatar, bio: "Georgina Garza is a junior computer science and dance double major at UT Austin", commits: 0, issues: 0, unit_tests: 0},
         {name: "Gerardo Mares", gitlab_name: "Gerardo Mares", role: "Developer", image: avatar, bio: "Gerardo Mares is a senior computer science major with a minor in business at UT Austin", commits: 0, issues: 0, unit_tests: 0},
         {name: "Jacob Zillifro", gitlab_name: "JZillifro", role: "Developer", image: avatar, bio: "Jacob is a junior computer science major at UT Austin", commits: 0, issues: 0, unit_tests: 0},
         {name: "Paul Purifoy", gitlab_name: "Paul Purifoy", role: "Developer", image: avatar, bio: "my name is Paul", commits: 0, issues: 0, unit_tests: 0},
         {name: "Edgar Marroquin", gitlab_name: "Edgar Marroquin", role: "Developer", image: avatar, bio: "my name is Edgar", commits: 0, issues: 0, unit_tests: 0}
      ],
      issues: [],
      commits: 0
    };
  }

  componentDidMount() {
    fetch('https://gitlab.com/api/v4/projects/8623652/repository/contributors')
   .then(response => response.json())
   .then(contributors_data => {
      var contributors = this.state.contributors;
      contributors.forEach(c => {
         const data = contributors_data.find(d => d.name === c.gitlab_name);
         if(data){
            c.commits = data.commits;
            c.email = data.email
         }
      });

      var commits = contributors.reduce(function(accumulator, contributor) {
         return accumulator + contributor.commits;
      }, 0);

      this.setState({contributors});
      this.setState({commits});
   })

    fetch('https://gitlab.com/api/v4/projects/8623652/issues')
    .then(issues => issues.json())
    .then(issues => {
      var contributors = this.state.contributors;
      contributors.forEach(c => {
         const data = issues.filter(i => i.author.name === c.gitlab_name);
         if(data){
            c.issues = data.length;
         }
      });

      this.setState({contributors});
      this.setState({issues});
   })

  };

  render() {
    return (
        <div className="container">
           <hr/>
           <h2>About</h2>
           <hr/>
           <Row className="row">
               <Col xs={12} sm={12} md={6} lg={6}>
                  <img src="https://openclipart.org/download/276483/1490609861.svg"
                       alt="home" className="img-fluid"/>
               </Col>
               <Col xs={12} sm={12} md={6} lg={6}>
                     <h2>About NPO Link</h2><hr/>
                     <p>NPO Link aims to help you learn more about nonprofits in your area
                     and how you can contribute. We provide a way for you to search nonprofits based
                     on location and category as well as see what non-profits exist for various categories
                     and what non-profits exist in a location.
                     </p>
               </Col>
           </Row>
           <hr/>
           <h2>Team</h2>
           <hr/>
           <Row className="row justify-content-center text-center">
            {
              this.state.contributors.map(contributor => (
                 <Col xs={12} sm={12} md={6} lg={4} className="pb-4">
                    <Card key={contributor.email}>
                        <CardImg top width="100%"
                        src={contributor.image}
                        className="card-img-top"
                        alt="Card image" />
                        <CardHeader>{contributor.name}</CardHeader>
                        <CardBody>
                          <CardSubtitle>{contributor.role}</CardSubtitle>
                          <hr/>
                          <CardText className="pt-2">
                             <p>{contributor.bio}</p>
                          </CardText>
                        </CardBody>
                        <CardFooter>
                        <p>
                        commits: {contributor.commits} <br/>
                        issues: {contributor.issues} <br/>
                        unit tests: {contributor.unit_tests}
                        </p></CardFooter>
                    </Card>
                 </Col>
              ))
            }
          </Row>
          <hr/>
          <h2>Details</h2>
          <hr/>
          <CardDeck className="pb-5 text-center justify-content-center">
            <Card>
               <CardHeader>Project Stats</CardHeader>
               <CardBody>
                <CardText className="pt-2">
                    <p>issues: {this.state.issues.length}
                    </p>
                    <p>commits: {this.state.commits}</p>
                    <p>unit tests: 0</p>
                </CardText>
               </CardBody>
            </Card>
            <Card>
               <CardHeader>Project Links</CardHeader>
               <CardBody>
                <CardText className="pt-2">
                    <p><a href="https://documenter.getpostman.com/view/5491513/RWgm3gY7">Postman API</a></p>
                    <p><a href="https://gitlab.com/gerardomares/npolink">GitLab Repository</a></p>
                </CardText>
               </CardBody>
            </Card>
            <Card>
               <CardHeader>Project Tools</CardHeader>
               <CardBody>
                <CardText className="pt-2">
                     <p>
                     React<br/>
                     Postman<br/>
                     GitLab<br/>
                     Bootstrap<br/>
                     Docker<br/>
                     AWS Elastic Beanstalk<br/>
                     AWS S3<br/>
                     Namecheap<br/>
                     Grammarly
                     </p>
                </CardText>
               </CardBody>
            </Card>
          </CardDeck>
       </div>
    );
  }
}

export default About;
