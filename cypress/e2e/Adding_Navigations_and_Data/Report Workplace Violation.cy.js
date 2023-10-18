/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  
cy.Login();
cy.open_Navigation();
cy.add_Navigation('T.Report Workplace Violation', 'Report Workplace Violation')
cy.find_navigation('T.Report Workplace Violation')
})


