import React from 'react';
import {PageHeader} from 'react-bootstrap';

export default class CategoryPage extends React.Component {
  render() {
    return (
      <div className="container">
        <PageHeader>
          <div>TITLE</div>
          <div><small>Subtext for header</small></div>
        </PageHeader>
        <div>
          IMAGE
        </div>
        <div>
          STATS
        </div>
        <div>
          LOCATION LIST
        </div>
        <div>
          NONPROFIT LIST
        </div>
      </div>
    )
  }
}
