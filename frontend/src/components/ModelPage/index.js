import React from 'react';
import {PageHeader, Grid, Row, Col} from 'react-bootstrap';
import ModelPanel from './ModelPanel.js';

export default class ModelPage extends React.Component {
  render() {
    return (
      <div className="container">
        <PageHeader>
          <div>Title</div>
          <div><small>Subtext for header</small></div>
        </PageHeader>

        <Grid>
          <Row>
            <Col xs={6} md={4}>
              <ModelPanel/>
            </Col>
            <Col xs={6} md={4}>
              <ModelPanel/>
            </Col>
            <Col xs={6} md={4}>
              <ModelPanel/>
            </Col>
          </Row>
        </Grid>
      </div>
    )
  }
}
