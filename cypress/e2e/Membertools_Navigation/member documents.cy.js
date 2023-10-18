/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  cy.Login();
 /* cy.open_Membertools_Navigation()
  cy.add_membertools('M.Member Documents', 'Member Documents')*/
  cy.find_navigation('M.Member Documents')
 /* cy.add_discount_type_button()
  cy.add_document_type('type 1')
  cy.add_document_type('type 2')
  cy.add_document_type('type 3')
  cy.view_discount_button()
  */
  //1
  cy.add_document_button()
  cy.add_document('Document 1(Industry)','type 1','Apple','https://www.google.com/','We are testing document 1 here.','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','member1.jpg')
  cy.sumbit_button()
 //2
 cy.add_document_button()
 //cy.add_document_button()

 cy.add_document(' Discount 2 ','type 2','','https://www.twitter.com/','We are testing documnets 2 here.','But the majority have suffered alteration in some form, by injected humour','member2.jpg')
 cy.sumbit_button()
 //3
 cy.add_document_button()
 cy.add_document('Discount 3','type 2','','https://www.facebook.com/','testing Document type 3 here.','','')
 cy.sumbit_button()

  //Edit Functionality
  cy.edit();

  //Clone Functionality
  cy.clone();
})
 