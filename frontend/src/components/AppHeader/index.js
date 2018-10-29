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
      <nav id="nav" style={{background: "#2b252c"}}>
        <ul>
          <li><a href="/">Home</a></li>
          {/* <li>
            <a href="#">Dropdown</a>
            <ul>
              <li><a href="#">Nonprofits</a></li>
              <li><a href="#">Categories</a></li>
              <li><a href="#">Etiam dolore nisl</a></li>
              <li>
                <a href="#">And a submenu &hellip;</a>
                <ul>
                  <li><a href="#">Lorem ipsum dolor</a></li>
                  <li><a href="#">Phasellus consequat</a></li>
                  <li><a href="#">Magna phasellus</a></li>
                  <li><a href="#">Etiam dolore nisl</a></li>
                </ul>
              </li>
              <li><a href="#">Veroeros feugiat</a></li>
            </ul>
          </li> */}
          <li><a href="/nonprofits">Nonprofits</a></li>
          <li><a href="/categories">Categories</a></li>
          <li><a href="/locations">Locations</a></li>
          <li><a href="/about">About</a></li>
        </ul>
      </nav>
      // <div>
      //   <Navbar color="light" light expand="md" style={{backgroundColor: "#6897bb"}}>
      //     <NavbarBrand href="/">NPOLink</NavbarBrand>
      //     <NavbarToggler onClick={this.toggle} />
      //     <Collapse isOpen={this.state.isOpen} navbar>
      //        <Nav className="mr-auto" navbar>
      //          <NavItem>
      //            <NavLink href='/'>Home</NavLink>
      //          </NavItem>
      //          <NavItem>
      //            <NavLink href='/nonprofits'>Non-profits</NavLink>
      //          </NavItem>
      //          <NavItem>
      //            <NavLink href='/categories'>Categories</NavLink>
      //          </NavItem>
      //          <NavItem>
      //            <NavLink href='/locations'>Locations</NavLink>
      //          </NavItem>
      //          <NavItem>
      //            <NavLink href='/about'>About</NavLink>
      //          </NavItem>
      //        </Nav>
      //     </Collapse>
      //   </Navbar>
      // </div>
    );
  }
}

export default AppHeader;
