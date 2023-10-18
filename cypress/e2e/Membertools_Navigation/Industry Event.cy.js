/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
  cy.Login();
    
  cy.open_Membertools_Navigation()
  cy.add_membertools('M.Industry Events', 'Industry Events')
  cy.find_navigation('M.Industry Events')
 
  //1
  cy.add_industry_news('Public Industry News 1!','We are testing Public Industry News','02adff02-47ee-477b-9651-4a11d70a090d','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','save.png')
  cy.sumbit_button()

  //2
  cy.add_industry_news('UnPublished Industry News 3!',' We are testing Unpublished Industry News','',' the majority have suffered alteration in some form, by injected humour','a.png')
  cy.unpublished()
  cy.sumbit_button()

 //3
 cy.add_industry_news('NEWS WITHOUT DESCRIPTION AND IMAGE','We are testing news without image and description.','02adff02-47ee-477b-9651-4a11d70a090d','','')
 cy.sumbit_button()
 
 //4
 cy.add_industry_news('Industry News Without Industry!',' We are testing Industry News','','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','nike.png')
 cy.sumbit_button()  
  
  //Edit Functionality
  cy.edit();

  //Clone Functionality
  cy.clone();
})
 