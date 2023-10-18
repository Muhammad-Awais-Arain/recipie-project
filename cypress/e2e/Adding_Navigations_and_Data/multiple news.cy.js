/// <reference types= "cypress"/>
it("passes", () => {
  cy.backend_link();

  cy.Login();
  cy.open_Navigation();
  cy.add_Navigation("T.Multiple News test!", "Multiple News");
  cy.find_navigation("T.Multiple News test!");

  //1
  cy.add_multiple_news(
    "Public Multiple News 1!",
    "We are testing Public Multiple News",
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s",
    "save.png"
  );
  cy.sumbit_button();

  //2
  cy.add_multiple_news(
    "Private Multiple News 2!",
    " We are testing Private Multiple News",
    "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour",
    "nike.png"
  );
  cy.private();
  cy.sumbit_button();

  //3
  cy.add_multiple_news(
    "UnPublished Multiple News 3!",
    " We are testing Unpublished Multiple News",
    " the majority have suffered alteration in some form, by injected humour",
    "a.png"
  );
  cy.unpublished();
  cy.sumbit_button();
  //4
  cy.add_multiple_news("NEWS WITHOUT DESCRIPTION AND IMAGE", "", "", "");
  cy.sumbit_button();

  //5
  cy.add_multiple_news(
    "NEWS WITHOUT IMAGE",
    "Testing without Image",
    "The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33",
    ""
  );
  cy.sumbit_button();

  //Edit Functionality
  cy.edit();

  //Clone Functionality
  cy.clone();
});
