import React from 'react';
import {Thumbnail, Button} from 'react-bootstrap';
const ModelPanel = ({
  id,
  image,
  title,
  description,
  type
}) => (
  <div className="container">
    <Thumbnail style={{maxWidth:"100%", maxHeight:"100%"}}>
      <img src={image} alt="242x200" style={{maxWidth:"100%", maxHeight:"100%"}} />
      <h3>{title}</h3>
      <p>{description}</p>
      <Button bsStyle="primary" href={type + "/" +  id}>Learn more</Button>
    </Thumbnail>
  </div>
);

export default ModelPanel;
