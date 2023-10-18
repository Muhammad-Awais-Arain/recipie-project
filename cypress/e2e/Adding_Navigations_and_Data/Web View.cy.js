/// <reference types= "cypress"/>
it('passes', () => {
cy.backend_link();
    
  cy.Login();
  cy.open_Navigation();
  cy.add_Navigation('Web View test!', 'Web View')
  cy.find_navigation('Web View test!')
//1
  cy.add_webview('Web View Unpublished!','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','save.png')
  cy.unpublished()
  cy.private()
  cy.sumbit_button()

//2
  cy.add_webview('Web View Published!','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','nike.png')
  cy.sumbit_button()
  cy.yes()

  //Edit Functionality
cy.edit();

//Clone Functionality
cy.clone();
})
 