
/// <reference types= "cypress"/>
it('passes', () => {
   cy.backend_link();
  cy.Login();
  cy.open_InformationSettings();
   

    cy.delete_Navigation('Info.Contact Support!');

    
  
})





