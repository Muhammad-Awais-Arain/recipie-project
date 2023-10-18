/// <reference types= "cypress"/>
it('passes', () => {
cy.backend_link();
    
  cy.Login();
  cy.open_Navigation();
  cy.add_Navigation('Gallery Test!', 'Gallery')
  cy.find_navigation('Gallery Test!')



  
//1
  cy.add_gallery('Image 1','We are Testing here','save.png');
 // cy.add_to_slider();
  cy.sumbit_button();
  
//2
cy.add_gallery('Image 2','SQA is doing gallery testing so kindly ignore','a.png');
cy.unpublished();
cy.sumbit_button();
//3
cy.add_gallery('Image 3','We are Testing here','nike.png');
cy.sumbit_button();

//4
cy.add_gallery('Image 4','SQA is doing gallery testing so kindly ignore','map.png')
cy.sumbit_button();

//Edit functionality to edit gallery
cy.edit_gallery()

cy.update_status_unpublished('Image 4')

})
 