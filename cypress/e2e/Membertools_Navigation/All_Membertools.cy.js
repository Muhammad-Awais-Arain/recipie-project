/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
  cy.Login() 
  cy.open_Membertools_Navigation()
  cy.add_membertools('M.Industry Events', 'Industry Events')
  cy.find_navigation('M.Industry Events')
 
  //1
  cy.add_industry_news('Public Industry News 1!','We are testing Public Industry News','','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','save.png')
  cy.sumbit_button()

  //2
  cy.add_industry_news('UnPublished Industry News 3!',' We are testing Unpublished Industry News','',' the majority have suffered alteration in some form, by injected humour','a.png')
  cy.unpublished()
  cy.sumbit_button()

 //3
 cy.add_industry_news('NEWS WITHOUT DESCRIPTION AND IMAGE','We are testing news without image and description.','','','')
 cy.sumbit_button()
 
 //4
 cy.add_industry_news('Industry News Without Industry!',' We are testing Industry News','','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','nike.png')
 cy.sumbit_button()  


 cy.open_Membertools_Navigation()
 cy.add_membertools('M.Industry News', 'Industry News')
 cy.find_navigation('M.Industry News')

 //1
 cy.add_industry_news('Public Industry News 1!','We are testing Public Industry News','','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','save.png')
 cy.sumbit_button()

 //2
 cy.add_industry_news('UnPublished Industry News 3!',' We are testing Unpublished Industry News','',' the majority have suffered alteration in some form, by injected humour','a.png')
 cy.unpublished()
 cy.sumbit_button()

//3
cy.add_industry_news('NEWS WITHOUT DESCRIPTION AND IMAGE','We are testing news without image and description.','','','')
cy.sumbit_button()
//4
cy.add_industry_news('Industry News Without Industry!',' We are testing Industry News','','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','nike.png')
cy.sumbit_button()  


cy.open_Membertools_Navigation()
cy.add_membertools('M.Event Test!', 'Event')

    cy.find_navigation('M.Event Test!')
    cy.add_event('Private Event Test', 'Dolmen Mall','Automation Testing for Private event.','')
    cy.private()
    cy.sumbit_button()
//2
    cy.add_event('Public Event Test', 'Shanaz Arcade, Shaheed-e-Millat Rd, Delhi Mercantile Society, Karachi, Karachi City, Sindh','Automation Testing for Public event','nike.png')
    cy.sumbit_button()
        


    cy.open_Membertools_Navigation()
    cy.add_membertools('M.Find My Elected Officials!', 'Find My Elected Officials')
    cy.find_navigation('M.Find My Elected Officials!')


       
cy.open_Membertools_Navigation()
cy.add_membertools('M.Multiple Web Links', 'Multiple Web Links')
cy.find_navigation('M.Multiple Web Links')

cy.add_weblinks('GOOGLE', 'https://www.google.com/' )
cy.add_weblinks('Twitter', 'https://twitter.com/' )
cy.add_weblinks('Facebook', 'https://www.facebook.com/')
cy.add_weblinks('LinkedIn', 'https://www.linkedin.com/login' )



cy.open_Membertools_Navigation()
cy.add_membertools('M.Report Workplace Violation!', 'Report Workplace Violation')
cy.find_navigation('M.Report Workplace Violation!')



cy.open_Membertools_Navigation()
cy.add_membertools('M.Union Representative!', 'Union Representative')
cy.find_navigation('M.Union Representative!')

 //1
 cy.add_membertools_unionrepresentaive('Public Union Representative 1!','SQA','989765213','123456789','123','Hassan@gmail.com','','Time Square, Olympian Islah-ud-Din Rd, Block 6, Gulshan-e-Iqbal','https://www.google.com/','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','member1.jpg')
 cy.sumbit_button()

//2
 cy.add_membertools_unionrepresentaive('PRIVATE Union Representative 2!','SQA','323452','2213456','543','sqa@gmail.com','','118 F-1 Main, Rashid Minhas Rd, Gulshan-e-Iqbal, Karachi, 75300','',' If you are going to use a passage of Lorem Ipsum, All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet','member2.jpg')
 cy.private()
 cy.sumbit_button()

//3
   cy.add_membertools_unionrepresentaive('UnPublished Union Representative 3!','Developer','89452','0913456','543','unpublished@gmail.com','','118 F-1 Main, Rashid Minhas Rd, Gulshan-e-Iqbal, Karachi, 75300','','this tend to repeat predefined chunks as necessary, making this the first true generator on the Internet','member4.jpg')
   cy.unpublished()
   cy.sumbit_button()
 
//4
   cy.add_membertools_unionrepresentaive('Representative(Without picture & description) !','Designer','753252','','','unpublished@gmail.com','','Tariq Rd, Delhi Society Delhi CHS PECHS, Karachi, Karachi City, Sindh 75400','','','')
   cy.sumbit_button()
 

   cy.open_Membertools_Navigation()
   cy.add_membertools('M.Web Link Test!', 'Web Link')
   cy.find_navigation('M.Web Link Test!')
   cy.add_weblinks('GOOGLE', 'https://www.google.com/' )


 cy.open_Membertools_Navigation()
 cy.add_membertools('M.Work Schedule Test!', 'Work Schedule')
 cy.find_navigation('M.Work Schedule Test!')
  

 cy.open_Membertools_Navigation()
 cy.add_membertools('M.Member Documents', 'Member Documents')
 cy.find_navigation('M.Member Documents')
 cy.add_discount_type_button()
 cy.add_document_type('type 1')
cy.add_document_type('type 2')
 cy.add_document_type('type 3')
 cy.view_discount_button()
 //1
 cy.add_document_button()
 cy.add_document('Document 1(Industry)','type 1','','https://www.google.com/','We are testing document 1 here.','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','member1.jpg')
 cy.sumbit_button()
//2
cy.add_document_button()
cy.add_document_button()
cy.add_document_button()


cy.add_document(' Discount 2 ','type 2','','https://www.twitter.com/','We are testing documnets 2 here.','But the majority have suffered alteration in some form, by injected humour','member2.jpg')
cy.sumbit_button()
//3
cy.add_document_button()
cy.add_document('Discount 3','type 2','','https://www.facebook.com/','testing Document type 3 here.','','')
cy.sumbit_button()




cy.open_Membertools_Navigation()
   
    
cy.get('#add_menu_navigation').click()
cy.get('[style=""] > :nth-child(1) > :nth-child(1) > #kt_portlet_tools_4 > .kt-portlet__head > .kt-portlet__head-label > .w-100').click()
cy.get('[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > :nth-child(1) > .col-lg-8 > .row > .col > .form-control').clear()   
cy.get('[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > :nth-child(1) > .col-lg-8 > .row > .col > .form-control').type('M.Sub Menu Test!')
cy.get('[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > :nth-child(1) > .col-lg-8 > .dropdown > .btn').click({force:true})
cy.get("a[role='option']").each(function ($ele,index,list){

if ($ele.text() === 'Sub Menu'){
    cy.log("found element")
    cy.wrap($ele).click({force: true})

}




} )
cy.get('[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > #inner-repeater > .kt-portlet__foot > .row > .col-lg-10 > .btn').dblclick().dblclick().click()
//1
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(1) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__head').click()
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(1) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').clear()

cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(1) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').type('M.Sub.Multiple Web Links',{force: true} )
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(1) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > .form-group > .col-lg-8 > .dropdown > .btn').click()
cy.focused('.dropdown-item').contains('Multiple Web Links').click()
//2
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(2) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__head').click()
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(2) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').clear()

cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(2) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').type('M.Sub.Report Violation',{force: true} )
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(2) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > .form-group > .col-lg-8 > .dropdown > .btn').click()
cy.focused('.dropdown-item').contains('Report Workplace Violation').click()

//3
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(3) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__head').click()
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(3) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').clear()

cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(3) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').type('M.Sub.Webview',{force: true} )
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(3) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > .form-group > .col-lg-8 > .dropdown > .btn').click()
cy.focused('.dropdown-item').contains('Web View').click()

//4
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(4) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__head').click()
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(4) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').clear()

cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(4) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').type('M.Sub.FMEO',{force: true})
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(4) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > .form-group > .col-lg-8 > .dropdown > .btn').click()
cy.focused('.dropdown-item').contains('Find My Elected Officials').click()

//5
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(5) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__head').click()
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(5) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').clear()

cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(5) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > .form-group > .col-lg-8 > .row > .col > .form-control').type('M.Sub.WorkSchedule',{force: true})
cy.get('[kt-hidden-height="279"] > #inner-repeater > .kt_sortable_child_portlets > :nth-child(5) > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > .form-group > .col-lg-8 > .dropdown > .btn').click()
cy.focused('.dropdown-item').contains('Work Schedule').click()



cy.get('#kt_navigation_submit').click()
cy.wait(10000)



cy.get('#kt_aside_mobile_toggler').click()
cy.get('#kt_aside_menu').contains('M.Sub Menu Test!').click()
//
cy.get('#kt_aside_menu').contains('M.Sub.Multiple Web Links').click()

//1
cy.get('.table_button_section > .btn-success').click()
cy.wait(1500)


cy.get('#title').type('Twitter')
cy.wait(1000)
cy.get('#link').type('https://twitter.com/')
cy.get('#web_link_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success').click()

//2
cy.get('.table_button_section > .btn-success').click()
cy.wait(1000)

cy.get('#title').type('Facebook')
cy.wait(1000)

cy.get('#link').type('https://www.facebook.com/')
cy.get('#web_link_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success').click()

//3
cy.get('.table_button_section > .btn-success').click()
cy.wait(1000)

cy.get('#title').type('LinkedIn')
cy.wait(1000)

cy.get('#link').type('https://www.linkedin.com/login')
cy.get('#web_link_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success').click()

//4
cy.get('.table_button_section > .btn-success').click()
cy.wait(1000)

cy.get('#title').type('Instagram')
cy.wait(1000)

cy.get('#link').type('https://www.instagram.com/accounts/login/')
cy.get('#web_link_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success').click()
cy.wait(2000)


//REPORT WORKPLACE VIOLATION
cy.get('#kt_aside_mobile_toggler').click()
cy.get('#kt_aside_menu').contains('M.Sub.Report Violation').click({force: true})

//WEB VIEW
cy.get('#kt_aside_mobile_toggler').click()
cy.get('#kt_aside_menu').contains('M.Sub.Webview').click({force: true})

//1
cy.get('a > .btn').click()
cy.get(':nth-child(2) > .col-lg-10 > .form-control').type('Web View Testing')
cy.get('iframe.cke_wysiwyg_frame').then($iframe => {
    const $editable = $iframe.contents().find('.cke_editable')
    cy.wrap($editable).type('Lorem Ipsum is simply dummy text of  Ipsum has been  and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960 with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
  })
cy.get('#kt_dropzone_1').attachFile('save.png', { subjectType: 'drag-n-drop' });
cy.get('.bootstrap-switch-id-kt_switch_1 > .bootstrap-switch-container > .bootstrap-switch-label').click({force:true})
cy.get(':nth-child(8) > .col-lg-4 > .bootstrap-switch-off > .bootstrap-switch-container > .bootstrap-switch-label').click()
cy.get('.col-lg-4 > .btn').click()

// 2
cy.get('a > .btn').click()
cy.get(':nth-child(2) > .col-lg-10 > .form-control').type('Web View Testing')
cy.get('iframe.cke_wysiwyg_frame').then($iframe => {
    const $editable = $iframe.contents().find('.cke_editable')
    cy.wrap($editable).type('Lorem Ipsum is simply dummy text of  Ipsum has been  and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960 with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
  })
cy.get('#kt_dropzone_1').attachFile('nike.png', { subjectType: 'drag-n-drop' });
cy.get('.col-lg-4 > .btn').click()
cy.get('.swal2-confirm').click()
cy.wait(4000)
//FIND MY ELECTED OFFICIALS
cy.get('#kt_aside_mobile_toggler').click()
cy.get('#kt_aside_menu').contains('M.Sub.FMEO').click()

//WORKSCHEDULE
cy.get('#kt_aside_mobile_toggler').click()
cy.get('#kt_aside_menu').contains('M.Sub.WorkSchedule').click()


cy.open_Membertools_Navigation()
cy.add_membertools('M.Web View Test!', 'Web View')

cy.find_navigation('M.Web View Test!')
//1
cy.add_webview('Web View Unpublished!','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s','save.png')
cy.unpublished()
cy.private()
cy.sumbit_button()

//2
cy.add_webview('Web View Published!','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour','nike.png')
cy.sumbit_button()
cy.yes()

})
 