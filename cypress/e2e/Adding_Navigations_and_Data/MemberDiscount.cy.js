/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  cy.Login();
        
   cy.open_Navigation();
   cy.add_Navigation('T.Member Discount!', 'Member Discount')
   cy.find_navigation('T.Member Discount!')
   cy.add_discount_type_button()
   cy.add_discount_type('type 1')
   cy.add_discount_type('type 2')
   cy.add_discount_type('type 3')
   cy.view_discount_button()
   //1
   cy.add_discount_button()
   cy.add_discount('Discount 1','type 1','https://www.google.com/','We are testing Bills here.','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','member1.jpg')
   cy.sumbit_button()
   //2
   cy.add_discount_button()
   cy.add_discount('Private Discount 2 ','type 1','https://www.twitter.com/','We are testing private Bills here.','But the majority have suffered alteration in some form, by injected humour','member2.jpg')
   cy.private()
   cy.sumbit_button()
   //3
   cy.add_discount_button()
   cy.add_discount('Discount 3','type 2','https://www.facebook.com/','testing Bills type 2 here.','','')
   cy.sumbit_button()
   //4
   cy.add_discount_button()
   cy.add_discount('Discount 4','type 3','https://www.youtube.com/','We are testing Bills type 3 here.','Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old','member4.jpg')
   cy.sumbit_button()
   //5
   cy.add_discount_button()
   cy.add_discount('Discount 5 ','','','he online encyclopedia project Wikipedia is the most popular wiki-based website, and is one of the most widely viewed sites in the world, having been ranked in the top twenty since 2007','member5.jpg')
   cy.sumbit_button()
   
//Edit Functionality
cy.edit();

//Clone Functionality
cy.clone();
      
  
   
 })