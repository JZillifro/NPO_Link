import React from 'react';
import {PageHeader} from 'react-bootstrap';

export default class LocationPage extends React.Component {
  render() {
    return (
      <div className="container">
        <PageHeader>
          <div>TITLE</div>
          <div><small>Subtext for header</small></div>
        </PageHeader>
        <div>
          MAP HERE
        </div>
        <div>
          STATS
        </div>
        <div>
          NONPROFIT LIST PER CITY
        </div>
        <div>
          CATEGORY LIST PER CITY
        </div>
      </div>
    )
  }
}
