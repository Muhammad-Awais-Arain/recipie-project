/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  
cy.Login();
cy.open_Navigation();
cy.add_Navigation('T.SBS (Direct Vote Live)', 'SBS (Direct Vote Live)')
cy.find_navigation('T.SBS (Direct Vote Live)')
})


