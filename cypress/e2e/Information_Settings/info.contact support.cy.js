/// <reference types= "cypress"/>
it('passes', () => {
   cy.backend_link();  
   cy.Login();
   cy.open_InformationSettings();
  cy.add_Info_Navigation('Info.Contact Support!','Contact Support');

  cy.add_Info_Navigation('Info.Contact Support!','Contact Support');

  

})