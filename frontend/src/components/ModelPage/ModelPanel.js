import React from 'react';
import {Thumbnail, Button} from 'react-bootstrap';
//
// export default class ModelPanel extends React.Component {
//   render() {
//     return (
//       <div className="container">
//         <Thumbnail style={{border: "1px solid #ddd", maxWidth:"100%", maxHeight:"100%"}}>
//           <img src="https://pbs.twimg.com/profile_images/948761950363664385/Fpr2Oz35_400x400.jpg" alt="242x200" style={{border: "1px solid #ddd", maxWidth:"100%", maxHeight:"100%"}} />
//           <h3>Thumbnail label</h3>
//           <p>Description</p>
//           <p>
//             <Button bsStyle="primary" href="locations/Austin">Button</Button>
//           </p>
//         </Thumbnail>
//       </div>
//     )
//   }
// }

const ModelPanel = ({
  id,
  image,
  title,
  description
}) => (
  <div className="container">
    <Thumbnail style={{maxWidth:"100%", maxHeight:"100%"}}>
      <img src={image} alt="242x200" style={{maxWidth:"100%", maxHeight:"100%"}} />
      <h3>{title}</h3>
      <p>{description}</p>
      <p>
        <Button bsStyle="primary" href="locations/Austin">Learn more ></Button>
      </p>
    </Thumbnail>
  </div>
);

export default ModelPanel;
