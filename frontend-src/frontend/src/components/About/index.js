import React, { Component } from 'react'
import { Card, CardBody, CardImg, CardText, CardSubtitle, Row, Col , CardDeck, CardHeader, CardFooter} from 'reactstrap'

const gerardo = require("./../../gerardo.jpg")
const georgina = require("./../../georgina.jpg")
const edgar = require("./../../edgar.jpg")
const jacob = require("./../../jacob.jpg")
const paul = require("./../../bff.jpg")

class About extends Component {
  constructor(props) {
    super(props);
    this.state = {
      contributors: [
         {name: "Georgina Garza", gitlab_name: "Georgina Garza", role: "Developer", image: georgina, bio: " Georgina Garza is a junior computer science and dance double major at UT Austin", commits: 0, issues: 0, unit_tests: 18},
         {name: "Gerardo Mares", gitlab_name: "Gerardo Mares", role: "Developer", image: gerardo, bio: "Gerardo Mares is a senior computer science major with a minor in business at UT Austin", commits: 0, issues: 0, unit_tests: 36},
         {name: "Jacob Zillifro", gitlab_name: "JZillifro", role: "Developer", image: jacob, bio: "Jacob is a junior computer science major at UT Austin", commits: 0, issues: 0, unit_tests: 0},
         {name: "Paul Purifoy", gitlab_name: "pmpurifoy", role: "Developer", image: paul, bio: "Paul is a junior computer science major at UT Austin", commits: 0, issues: 0, unit_tests: 0},
         {name: "Edgar Marroquin", gitlab_name: "Artsandwitchcraft", role: "Developer", image: edgar, bio: "Edgar Marroquin is a senior computer science and biochemistry double major at UT Austin. His major responsibilites include API management and integration.", commits: 0, issues: 0, unit_tests: 36}
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
         c.commits = contributors_data.filter(d => d.name === c.gitlab_name)
                                      .map(data => data.commits)
                                      .reduce((acc, val) => acc + val, 0);
      });

      var commits = contributors.reduce((acc, c) => acc + c.commits, 0);

      this.setState({contributors});
      this.setState({commits});
   })

    fetch('https://gitlab.com/api/v4/projects/8623652/issues?state=closed')
    .then(issues => issues.json())
    .then(issues => {
      var contributors = this.state.contributors;
      contributors.forEach(c => {
         const data = issues.filter((issue) => issue.assignees.filter((assignee) => (assignee.name === c.name)).length > 0);
         if(data.length > 0){
            c.issues = data.length;
         }
      });

      this.setState({contributors});
      this.setState({issues});
   })

  };

  render() {
    return (
      <div className="wrapper style1" style={{color: "rgb(43, 37, 44)"}}>
        <section id="features" className="container special">
          <header>
            <h2>About</h2>
            <p>NPO Link aims to help you learn more about nonprofits in your area
                           and how you can contribute. We provide a way for you to search nonprofits based
                           on location and category as well as see what non-profits exist for various categories
                           and what non-profits exist in a location.</p>
          </header>
           <Row className="row justify-content-center text-center">
            {
              this.state.contributors.map((contributor) => (
                 <Col key={contributor.name + "-col"} xs={12} sm={12} md={6} lg={4} className="pb-4 d-flex align-items-stretch">
                    <Card>
                        <CardImg top width="100%"
                        src={contributor.image}
                        className="card-img-top"
                        alt="Card image" />
                        <CardHeader>{contributor.name}</CardHeader>
                        <CardBody>
                          <CardSubtitle>{contributor.role}</CardSubtitle>
                          <CardText className="pt-2">
                             {contributor.bio}
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
        </section>
        <section id="details" className="container special">
           <CardDeck className="pb-5 text-center justify-content-center">
             <Card>
                <CardHeader>Project Stats</CardHeader>
                <CardBody>
                <CardText className="pt-2">
                     issues: {this.state.issues.length}<br/>
                     commits: {this.state.commits}<br/>
                     unit tests: 90
                </CardText>
                </CardBody>
             </Card>
             <Card>
                <CardHeader>Project Links</CardHeader>
                <CardBody>
                <CardText className="pt-2">
                     <a href="https://documenter.getpostman.com/view/5491513/RzZ3K1zY">Postman API</a>
                </CardText>
                <CardText className="pt-2">
                     <a href="https://gitlab.com/gerardomares/npolink">GitLab Repository</a>
                </CardText>
                <CardText className="pt-2">
                     <a href="/visuals/all">Visualizations</a>
                </CardText>
                </CardBody>
             </Card>
             <Card>
                <CardHeader>Project Tools</CardHeader>
                <CardBody>
                <CardText className="pt-2">
                     React<br/>
                     Postman<br/>
                     GitLab<br/>
                     Bootstrap<br/>
                     Docker<br/>
                     AWS Elastic Beanstalk<br/>
                     AWS S3<br/>
                     Namecheap<br/>
                     Grammarly
                </CardText>
                </CardBody>
             </Card>
           </CardDeck>
        </section>
       </div>
    );
  }
}

export default About;
