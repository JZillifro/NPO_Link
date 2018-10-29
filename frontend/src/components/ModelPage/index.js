import React from 'react';
import NPSection from './NPSection.js'
import LSection from './LSection.js'
import CSection from './CSection.js'

export default class ModelPage extends React.Component {
  constructor(props) {
    super(props)
    this.state = {}
  }

  render() {
    return(
      <div className="wrapper style1" style={{color: "rgb(43, 37, 44)"}}>

        <section id="features" className="container special">
          <header>
            <h2>{this.props.match.params.title}</h2>
            <p>Ipsum volutpat consectetur orci metus consequat imperdiet duis integer semper magna.</p>
          </header>
          <div className="row">
            {
              this.props.match.params.title === "nonprofits" && <NPSection type={this.props.match.params.title} />
            }
            {
              this.props.match.params.title === "categories" && <CSection type={this.props.match.params.title} />
            }
            {
              this.props.match.params.title === "locations" && <LSection type={this.props.match.params.title} />
            }
          </div>
        </section>

      </div>
    );
  }
}
