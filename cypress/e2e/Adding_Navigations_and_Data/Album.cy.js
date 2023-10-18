/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
  cy.Login();
  //cy.two_factor_code();
  
 cy.open_Navigation();
 cy.add_Navigation('Test new album!', 'Album')
  cy.find_navigation('Test new album!')


//Album 1:
cy.add_album('New album test22');
cy.sumbit_button();
cy.select_album('New album test22');
cy.add_gallery('Image 1','We are Testing here','save.png');
cy.sumbit_button();
cy.add_gallery('Image 2','SQA is doing gallery testing so kindly ignore','a.png');
cy.unpublished();
cy.sumbit_button();
cy.add_Cover_photo('Image 1');
cy.back();

//Edit functionality to edit Album
cy.edit_gallery()

///ALBUM 2:
cy.add_album('New test album 2');
cy.unpublished();
cy.sumbit_button();
cy.select_album('New test album 2');
cy.add_gallery('A.image 1','We are Testing here','nike.png');
cy.sumbit_button();
cy.add_gallery('A.cover 2','SQA is doing gallery testing so kindly ignore','map.png')
cy.sumbit_button();

cy.add_Cover_photo('A.image 1');
cy.back();

//UnPublished by select all:
cy.update_status_unpublished('New test album 2')

//Published by select all:
// cy.update_status_published('New test album 2')


})
 