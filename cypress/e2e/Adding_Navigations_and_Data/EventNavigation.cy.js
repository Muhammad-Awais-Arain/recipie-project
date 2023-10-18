/// <reference types= "cypress"/>
it('passes', () => {
 cy.backend_link();
  cy.Login();
  cy.open_Navigation();
 cy.add_Navigation('Test neww Event!', 'Event')

    cy.find_navigation('Test neww Event!')
   
    cy.add_event('Private Event Test', 'Dolmen Mall','Automation Testing for Private event.','')
    cy.private()
    cy.sumbit_button()
    
//2
    cy.add_event('Public Event Test', 'Shanaz Arcade, Shaheed-e-Millat Rd, Delhi Mercantile Society, Karachi, Karachi City, Sindh','Automation Testing for Public event','nike.png')
    cy.sumbit_button()
    
  //Edit Functionality
 cy.edit();

  //Clone Functionality
  cy.clone();
     })

     