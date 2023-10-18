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
        
   
        
  cy.open_Navigation();
  cy.add_Navigation('T.Find My Elected Officials', 'Find My Elected Officials')
  cy.find_navigation('T.Find My Elected Officials')
 
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


cy.update_status_unpublished('Image 4')



cy.open_Navigation();
 cy.add_Navigation('T.Legislative Bill!', 'Legislative Bill')
 
   cy.find_navigation('T.Legislative Bill!')

    cy.add_legislative_bills('Bill 1!','We are testing Bill 1.','Where can I get some? There are many variations of passages of Lorem Ipsu.','Next hearing will be on Friday'
    ,'https://www.facebook.com/','It has been the industrys standard dummy text scrambled it to make a type specimen book.'
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

      
   cy.open_Navigation();
   cy.add_Navigation('T.Multiple News!', 'Multiple News')
   cy.find_navigation('T.Multiple News!')
   
   //1
   cy.add_multiple_news('Public Multiple News 1!','We are testing Public Multiple News','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','save.png')
   cy.sumbit_button()
 
  //2
   cy.add_multiple_news('Private Multiple News 2!',' We are testing Private Multiple News','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','nike.png')
   cy.private()
   cy.sumbit_button()
 
  //3
  cy.add_multiple_news('UnPublished Multiple News 3!',' We are testing Unpublished Multiple News',' the majority have suffered alteration in some form, by injected humour','a.png')
  cy.unpublished()
  cy.sumbit_button()
  //4
  cy.add_multiple_news('NEWS WITHOUT DESCRIPTION AND IMAGE','','','')
  cy.sumbit_button()
 
  //5
  cy.add_multiple_news('NEWS WITHOUT IMAGE','Testing without Image','The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33','')
  cy.sumbit_button()



  cy.open_Navigation();
cy.add_Navigation('Organize My WorkPlace Test!', 'Organize My Workplace')
cy.find_navigation('Organize My WorkPlace Test!')



cy.open_Navigation();
cy.add_Navigation('T.Multiple Web Links!', 'Multiple Web Links')
cy.find_navigation('T.Multiple Web Links!') 

cy.add_weblinks('GOOGLE', 'https://www.google.com/' )
cy.add_weblinks('Twitter', 'https://twitter.com/' )
cy.add_weblinks('Facebook', 'https://www.facebook.com/')
cy.add_weblinks('LinkedIn', 'https://www.linkedin.com/login' )



cy.open_Navigation();
cy.add_Navigation('T.Report Workplace Violation', 'Report Workplace Violation')
cy.find_navigation('T.Report Workplace Violation')

cy.open_Navigation();
cy.add_Navigation('T.SBS (Direct Vote Live)', 'SBS (Direct Vote Live)')
cy.find_navigation('T.SBS (Direct Vote Live)')


cy.open_Navigation();

  cy.add_Navigation('T.Social Media Links!', 'Social Media')
  cy.find_navigation('T.Social Media Links!')
  cy.add_social_media_link('Facebook','https://www.facebook.com/')

  cy.add_social_media_link('Twitter','https://twitter.com/')


  cy.open_Navigation();
  cy.add_Navigation('T.Union Representative!', 'Union Representative')
  
   cy.find_navigation('T.Union Representative!')
 //1
   cy.add_unionrepresentaive('Public Union Representative 1!','SQA','989765213','123456789','123','Hassan@gmail.com','Time Square, Olympian Islah-ud-Din Rd, Block 6, Gulshan-e-Iqbal','https://www.google.com/','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','member1.jpg')
   cy.sumbit_button()
 
 //2
   cy.add_unionrepresentaive('PRIVATE Union Representative 2!','SQA','323452','2213456','543','sqa@gmail.com','118 F-1 Main, Rashid Minhas Rd, Gulshan-e-Iqbal, Karachi, 75300','',' If you are going to use a passage of Lorem Ipsum, All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet','member2.jpg')
   cy.private()
   cy.sumbit_button()
 
 //3
     cy.add_unionrepresentaive('UnPublished Union Representative 3!','Developer','89452','0913456','543','unpublished@gmail.com','118 F-1 Main, Rashid Minhas Rd, Gulshan-e-Iqbal, Karachi, 75300','','this tend to repeat predefined chunks as necessary, making this the first true generator on the Internet','member4.jpg')
     cy.unpublished()
     cy.sumbit_button()
   
 //4
     cy.add_unionrepresentaive('Representative(Without picture & description) !','Designer','753252','','','unpublished@gmail.com','Tariq Rd, Delhi Society Delhi CHS PECHS, Karachi, Karachi City, Sindh 75400','','','')
     cy.sumbit_button()
  

    


  cy.open_Navigation();
  cy.add_Navigation('T.Web Link!', 'Web Link')
  cy.find_navigation('T.Web Link!') 
  cy.add_weblinks('GOOGLE', 'https://www.google.com/' )

  cy.open_Navigation();

  cy.add_Navigation('T.Work Schedule!', 'Work Schedule')
  cy.find_navigation('T.Work Schedule!')

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
  cy.screenshot()

})
 
        