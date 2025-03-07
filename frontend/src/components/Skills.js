import React, { useState, useEffect } from 'react';
import { Container, Row, Col, ProgressBar } from 'react-bootstrap';
import axios from 'axios';

function Skills() {
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSkills = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/skills');
        const groupedSkills = response.data.reduce((acc, skill) => {
          if (!acc[skill.category]) {
            acc[skill.category] = [];
          }
          acc[skill.category].push(skill);
          return acc;
        }, {});
        setSkills(groupedSkills);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching skills:', error);
        setLoading(false);
      }
    };

    fetchSkills();
  }, []);

  if (loading) {
    return (
      <Container className="text-center mt-5">
        <h2>Loading skills...</h2>
      </Container>
    );
  }

  return (
    <Container className="skills-container py-5">
      <h2 className="text-center mb-5">Technical Skills</h2>
      {Object.entries(skills).map(([category, categorySkills]) => (
        <div key={category} className="mb-5">
          <h3 className="mb-4">{category}</h3>
          <Row xs={1} md={2} className="g-4">
            {categorySkills.map((skill) => (
              <Col key={skill.id}>
                <div className="skill-item mb-3">
                  <div className="d-flex justify-content-between mb-1">
                    <span>{skill.name}</span>
                    <span>{skill.proficiency}%</span>
                  </div>
                  <ProgressBar 
                    now={skill.proficiency} 
                    variant={skill.proficiency >= 80 ? "success" : 
                            skill.proficiency >= 60 ? "info" : 
                            skill.proficiency >= 40 ? "warning" : "danger"}
                  />
                </div>
              </Col>
            ))}
          </Row>
        </div>
      ))}
    </Container>
  );
}

export default Skills;
