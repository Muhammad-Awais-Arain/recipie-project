/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
    
  cy.Login();
    
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
 cy.get('#kt_aside_menu').contains('M.Sub.Report Violation').click()

//WEB VIEW
 cy.get('#kt_aside_mobile_toggler').click()
 cy.get('#kt_aside_menu').contains('M.Sub.Webview').click()
 
//1
 cy.get('a > .btn').click()
 cy.get(':nth-child(2) > .col-lg-10 > .form-control').type('Web View Testing')
 cy.get('.cke_wysiwyg_frame').its('0.contentDocument.body').type('Lorem Ipsum is simply dummy text of  Ipsum has been  and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960 with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
 cy.get('#kt_dropzone_1').attachFile('save.png', { subjectType: 'drag-n-drop' });
 cy.get('.bootstrap-switch-id-kt_switch_1 > .bootstrap-switch-container > .bootstrap-switch-label').click({force:true})
 cy.get(':nth-child(8) > .col-lg-4 > .bootstrap-switch-off > .bootstrap-switch-container > .bootstrap-switch-label').click()
 cy.get('.col-lg-4 > .btn').click()

// 2
cy.get('a > .btn').click()
cy.get(':nth-child(2) > .col-lg-10 > .form-control').type('Web View Testing')
cy.get('.cke_wysiwyg_frame').its('0.contentDocument.body').type('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960 with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
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

  })
  