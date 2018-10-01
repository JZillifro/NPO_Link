import React, { Component } from 'react';
import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink } from 'reactstrap';

class AppHeader extends Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  render() {
    return (
      <div>
        <Navbar color="light" light expand="md">
          <NavbarBrand href="/">NPOLink</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
             <Nav className="mr-auto" navbar>
               <NavItem>
                 <NavLink href='/'>Home</NavLink>
               </NavItem>
               <NavItem>
                 <NavLink href='/nonprofits'>Non-profits</NavLink>
               </NavItem>
               <NavItem>
                 <NavLink href='/categories'>Categories</NavLink>
               </NavItem>
               <NavItem>
                 <NavLink href='/locations'>Locations</NavLink>
               </NavItem>
               <NavItem>
                 <NavLink href='/about'>About</NavLink>
               </NavItem>
             </Nav>
          </Collapse>
        </Navbar>
      </div>
    );
  }
}

export default AppHeader;
