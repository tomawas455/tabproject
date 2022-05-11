import {Navbar,Nav} from 'react-bootstrap'
import {Container} from 'react-bootstrap';
import {Link} from 'react-router-dom';
function Header()
{
return (
            <div>
  <Navbar bg="dark" variant="dark">
    <Container>
    <Navbar.Brand href="#home">ZMITAC learning</Navbar.Brand>
    <Nav className="me-auto navbar_wrapper">
      <Link to="/login"> login </Link>
      <Link to="/register"> register </Link>
    </Nav>
    </Container>
  </Navbar>
            </div>
)
}

export default Header