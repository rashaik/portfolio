import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import { faExternalLinkAlt } from '@fortawesome/free-solid-svg-icons';
import API_BASE_URL from '../config';
import './Projects.css';

function Projects() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [loadedImages, setLoadedImages] = useState({});

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        console.log('Fetching from:', `${API_BASE_URL}/projects`); // Debug log
        const response = await axios.get(`${API_BASE_URL}/projects`);
        console.log('API Response:', response.data); // Debug log
        setProjects(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching projects:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  const handleImageLoad = (projectId) => {
    setLoadedImages(prev => ({
      ...prev,
      [projectId]: true
    }));
  };

  if (loading) {
    return (
      <Container className="text-center mt-5">
        <h2>Loading projects...</h2>
      </Container>
    );
  }

  if (error) {
    return (
      <Container className="text-center mt-5">
        <h2>Error loading projects</h2>
        <p className="text-danger">{error}</p>
      </Container>
    );
  }

  return (
    <Container className="projects-container py-5">
      <h2 className="text-center mb-5">My Projects</h2>
      <Row xs={1} md={2} lg={3} className="g-4">
        {projects && projects.length > 0 ? (
          projects.map((project) => (
            <Col key={project.id}>
              <Card className="h-100 project-card">
                {project.image_url && (
                  <div className="card-img-wrapper">
                    <Card.Img 
                      variant="top" 
                      src={project.image_url} 
                      alt={project.title}
                      className={`project-image ${loadedImages[project.id] ? 'loaded' : ''}`}
                      onLoad={() => handleImageLoad(project.id)}
                    />
                  </div>
                )}
                <Card.Body>
                  <Card.Title className="project-title">{project.title}</Card.Title>
                  <Card.Text className="project-description">{project.description}</Card.Text>
                  <div className="tech-stack">
                    {project.technologies && project.technologies.split(',').map((tech, index) => (
                      <span key={index} className="badge bg-secondary">
                        {tech.trim()}
                      </span>
                    ))}
                  </div>
                </Card.Body>
                <Card.Footer className="bg-transparent border-0 project-links">
                  {project.github_url && (
                    <a
                      href={project.github_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="btn btn-outline-dark"
                    >
                      <FontAwesomeIcon icon={faGithub} /> Code
                    </a>
                  )}
                  {project.live_url && (
                    <a
                      href={project.live_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="btn btn-primary"
                    >
                      <FontAwesomeIcon icon={faExternalLinkAlt} /> Live Demo
                    </a>
                  )}
                </Card.Footer>
              </Card>
            </Col>
          ))
        ) : (
          <Col xs={12} className="text-center">
            <p>No projects found. Please check back later!</p>
          </Col>
        )}
      </Row>
    </Container>
  );
}

export default Projects;
