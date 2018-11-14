import React from 'react';
import { Col, Dropdown, DropdownMenu, DropdownItem, DropdownToggle } from 'reactstrap';
import PropTypes from 'prop-types'

const propTypes = {
    onClick: PropTypes.func.isRequired,
    items: PropTypes.array.isRequired,
    value: PropTypes.string.isRequired,
    dropdownType: PropTypes.string.isRequired
}

class DropdownChoices extends React.Component {
  constructor(props) {
    super(props);
    this.toggle = this.toggle.bind(this);
    this.select = this.select.bind(this);
    this.state = {
      dropdownOpen: false,
      value : this.props.value
    };
  }

  toggle() {
    this.setState({
      dropdownOpen: !this.state.dropdownOpen
    });
  }

  select(event) {
    this.setState({
      dropdownOpen: !this.state.dropdownOpen,
      value: event.target.innerText
    }, () => {
      this.props.onClick(this.state.value);
      // this.toggle;
    })
  }

  render() {
    return (
      <Col>
         <Dropdown id={this.props.dropdownType + "_dropdown"} isOpen={this.state.dropdownOpen} toggle={this.toggle}>
           <DropdownToggle caret>
             {this.props.value}
           </DropdownToggle>
           <DropdownMenu className="scrollable-menu">
            {
               this.props.items.map((item) => (
                  <DropdownItem id={"selection_" + item} key={item} onClick={this.select }>{item}</DropdownItem>
               ))
            }
           </DropdownMenu>
         </Dropdown>
      </Col>
    );
  }
}

DropdownChoices.propTypes = propTypes;
export default DropdownChoices
