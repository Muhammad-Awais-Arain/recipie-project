/// <reference types= "cypress"/>
it('passes', () => {
cy.backend_link();
    
  cy.Login();
cy.open_Navigation();
 cy.add_Navigation('T.Legislative Bill!', 'Legislative Bill')
   cy.find_navigation('T.Legislative Bill!')

    cy.add_legislative_bills('Bill 1!','We are testing Bill 1.','Where can I get some? There are many variations of passages of Lorem Ipsu.','Next hearing will be on Friday'
    ,'https://www.facebook.com/','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text scrambled it to make a type specimen book.'
    ,'Hassan@gmail.com','save.png')
    cy.sumbit_button()

    //2
    cy.add_legislative_bills('Bill 2 Unpublished!','We are testing Bill 2.','Where can I get some? There are many variations.','Next hearing is on Tuesday'
    ,'https://www.google.com/','It has been the industrys standard dummy text scrambled it to make a type specimen book.'
    ,'Linkedunion@gmail.com','a.png')
    cy.unpublished()
    cy.sumbit_button()

    //3
    cy.add_legislative_bills('Bill 3 Private!','We are testing Bill 3.','Where can I get some? There are many variations.','Next hearing is on Thursday'
    ,'https://twitter.com/','We are testing Private Bill here........'
    ,'Linkedunion@gmail.com','map.png')
    cy.private()
    cy.sumbit_button()
    
     //4 
     cy.add_legislative_bills('Bill 4 Without Picture & Description! & Donation Link','We are testing Bill 4.','Where can I get some? There are many variations.','Next hearing is on Sunday'
     ,'','','','')
     cy.sumbit_button()

    //Edit Functionality
  cy.edit();

  //Clone Functionality
  cy.clone();


})
 