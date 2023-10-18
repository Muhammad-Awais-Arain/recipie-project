/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
    
  cy.Login();
  cy.open_Navigation();

  cy.add_Navigation('T.Work Schedule!', 'Work Schedule')
  cy.find_navigation('T.Work Schedule!')
})
 