/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  
cy.Login();
cy.open_Navigation();
cy.add_Navigation('Organize My WorkPlace Test!', 'Organize My Workplace')
cy.find_navigation('Organize My WorkPlace Test!')
})



