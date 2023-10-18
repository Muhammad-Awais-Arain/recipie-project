/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
cy.Login();

cy.open_Membertools_Navigation()
cy.add_membertools('M.Union Representative!', 'Union Representative')
cy.find_navigation('M.Union Representative!')
 //1
 
 cy.add_membertools_unionrepresentaive('Public Union Representative 1!','SQA','989765213','123456789','123','Hassan@gmail.com','002a6208-33de-4c34-9812-Fab2ec49bf8b','Time Square, Olympian Islah-ud-Din Rd, Block 6, Gulshan-e-Iqbal','https://www.google.com/','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','member1.jpg')
 cy.sumbit_button()

//2
 cy.add_membertools_unionrepresentaive('PRIVATE Union Representative 2!','SQA','323452','2213456','543','sqa@gmail.com','002a6208-33de-4c34-9812-Fab2ec49bf8b','118 F-1 Main, Rashid Minhas Rd, Gulshan-e-Iqbal, Karachi, 75300','',' If you are going to use a passage of Lorem Ipsum, All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet','member2.jpg')
 cy.private()
 cy.sumbit_button()

//3
   cy.add_membertools_unionrepresentaive('UnPublished Union Representative 3!','Developer','89452','0913456','543','unpublished@gmail.com','','118 F-1 Main, Rashid Minhas Rd, Gulshan-e-Iqbal, Karachi, 75300','','this tend to repeat predefined chunks as necessary, making this the first true generator on the Internet','member4.jpg')
   cy.unpublished()
   cy.sumbit_button()
 
//4
   cy.add_membertools_unionrepresentaive('Representative(Without picture & description) !','Designer','753252','','','unpublished@gmail.com','002a6208-33de-4c34-9812-Fab2ec49bf8b','Tariq Rd, Delhi Society Delhi CHS PECHS, Karachi, Karachi City, Sindh 75400','','','')
   cy.sumbit_button()
 
  //Edit Functionality
  cy.edit();

  //Clone Functionality
  cy.clone();

})
  