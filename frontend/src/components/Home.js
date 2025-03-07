import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub, faLinkedin } from '@fortawesome/free-brands-svg-icons';

function Home() {
  return (
    <Container className="home-container">
      <Row className="min-vh-100 align-items-center">
        <Col md={8} className="mx-auto text-center">
          <h1 className="display-3 mb-4">Welcome to My Portfolio</h1>
          <p className="lead mb-4">
            Full Stack Developer passionate about creating innovative web solutions
          </p>
          <div className="social-links mb-4">
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="mx-3">
              <FontAwesomeIcon icon={faGithub} size="2x" />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="mx-3">
              <FontAwesomeIcon icon={faLinkedin} size="2x" />
            </a>
          </div>
          <div className="cta-buttons">
            <Button as={Link} to="/projects" variant="primary" className="mx-2">
              View Projects
            </Button>
            <Button as={Link} to="/contact" variant="outline-primary" className="mx-2">
              Contact Me
            </Button>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
