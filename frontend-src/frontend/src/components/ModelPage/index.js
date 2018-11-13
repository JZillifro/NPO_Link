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
            <br/>
            {
              this.props.match.params.title === "Nonprofits" && <p>Nonprofit organizations are accountable to the donors, funders, volunteers, program recipients, and the public community.</p>
            }
            {
              this.props.match.params.title === "Categories" && <p>These are various types of nonprofit organizations.</p>
            }
            {
              this.props.match.params.title === "Locations" && <p>These are various cities which have nonprofit organizations.</p>
            }
          </header>
          <div className="row">
            {
              this.props.match.params.title === "Nonprofits" && <NPSection type={this.props.match.params.title} />
            }
            {
              this.props.match.params.title === "Categories" && <CSection type={this.props.match.params.title} />
            }
            {
              this.props.match.params.title === "Locations" && <LSection type={this.props.match.params.title} />
            }
          </div>
        </section>

      </div>
    );
  }
}
