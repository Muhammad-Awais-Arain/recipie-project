import "cypress-file-upload";


import "@4tw/cypress-drag-drop";
import "cypress-wait-until";

//************************** GNERAL *******************************//

//BACKEND LINK

Cypress.Commands.add("backend_link", () => {
  cy.visit("https://desibook.admin.linkedunion.org/");
});
//WEBSITE LINK
Cypress.Commands.add("website_link", () => {
  cy.visit("http://desibook.web.linkedunion.live/");
});

// Back
Cypress.Commands.add("back", () => {
  cy.get(".kt-portlet__head-wrapper > .btn-clean").click();
});

//LOGIN

Cypress.Commands.add("Login", () => {
  cy.get('input[name="email"]').type("luautomatedguru@linkedunion.com");
  cy.get('input[name="password"]').type("Automation@1234");
  cy.get(".kt-checkbox > span").click();
  cy.get("#kt_login_signin_submit").click();
  //2FA
  const values = ["3", "4", "5", "8", "7", "6"];

  cy.get("#phoneInput")
    .find('input[name="letters[]"]')
    .each(($input, index) => {
      if (index >= 0 && index <= 5) {
        cy.wrap($input).type(values[index]);
      }
    });
  cy.get("#kt_verify_two_factor_code").click();
});

//Delete ALL Navigation
Cypress.Commands.add("delete_Navigation", (name) => {
  cy.get(".kt-portlet__body")
    .contains(name, { matchCase: false })
    .closest(".kt-portlet__head-custom-color")
    .find("[data-repeater-delete]")
    .should("be.visible")
    .first()
    .click();
  cy.get("#kt_navigation_submit").should("be.visible").click();
  cy.wait(5000);
});

//SUBMIT button
Cypress.Commands.add("sumbit_button", () => {
  cy.get(".col-lg-4 > .btn").should("be.visible").click({ force: true });

  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});
//Published button
Cypress.Commands.add("published", () => {
  cy.get('input[name="publish"]').eq(0).click({ force: true });
});

//Unpublished button
Cypress.Commands.add("unpublished", () => {
  cy.get('input[name="publish"]').eq(1).click({ force: true });
});

//Private
Cypress.Commands.add("private", () => {
  cy.get('input[name="private"]').eq(1).click({ force: true });
});

//Public

Cypress.Commands.add("public", () => {
  cy.get('input[name="private"]').eq(0).click({ force: true });
});
//************* Edit ********************/
//Edit
Cypress.Commands.add("edit", () => {
  // Find the parent element <td> first and force it to become visible
  cy.get("td.kt-datatable__cell")
    .invoke("show")
    .find("button.btn.btn-clean.btn-icon.btn-sm.btn-icon-md")
    .first()
    .click();

  // cy.get("button.btn.btn-clean.btn-sm.btn-icon.btn-icon-md")
  //.first().should("be.visible").click({force:true});
  cy.get("a.kt-nav__link").contains("Edit").click({ force: true });
  cy.get(":nth-child(2) > .col-lg-10 > .form-control").clear();
  cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(" Edited");
  cy.get(".col-lg-4 > .btn").should("be.visible").click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

//Edit Multiple Weblinks
Cypress.Commands.add("edit_weblink", () => {
  cy.wait(2500);
  cy.get("button.btn.btn-clean.btn-sm.btn-icon.btn-icon-md")
    .first()
    .should("be.visible")
    .click({ force: true });
  cy.get("a.kt-nav__link").contains("Edit").click({ force: true });
  cy.wait(1500);
  cy.get("#title").clear();
  cy.get("#title").type(" Edited");
  cy.get(
    "#web_link_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success"
  ).click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

//Edit Social Media Links
Cypress.Commands.add("edit_socialmedia_link", () => {
  cy.wait(2500);
  cy.get("button.btn.btn-clean.btn-sm.btn-icon.btn-icon-md")
    .first()
    .should("be.visible")
    .click({ force: true });
  cy.get("a.kt-nav__link").contains("Edit").click({ force: true });
  cy.wait(1500);
  cy.get("#link")
    .clear()
    .type("https://www.linkedin.com/login", { force: true });
  cy.get(
    "#stay_connected_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success"
  ).click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

//Edit Album/Gallery
Cypress.Commands.add("edit_gallery", () => {
  cy.get("a.gallery_edit").first().click({ force: true });
  cy.get('.form-control[name="name"]').clear({ force: true });
  cy.get('.form-control[name="name"]').type(" Edited", { force: true });
  cy.get(".col-lg-4 > .btn").should("be.visible").click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

//************* Clone ********************/
//Clone
Cypress.Commands.add("clone", () => {
  // cy.get("button.btn.btn-clean.btn-sm.btn-icon.btn-icon-md")
  //   .first()
  //   .should("be.visible")
  //   .click({ force: true });
  cy.get("td.kt-datatable__cell")
  .invoke("show")
  .find("button.btn.btn-clean.btn-icon.btn-sm.btn-icon-md")
  .first()
  .click();
  
  cy.get("a.kt-nav__link").contains("Clone").click({ force: true });
  cy.get(":nth-child(2) > .col-lg-10 > .form-control").clear();
  cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(" CLoned");
  cy.get(".col-lg-4 > .btn").should("be.visible").click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

//Clone Multiple Weblinks
Cypress.Commands.add("clone_weblink", () => {
  cy.wait(2500);
  cy.get("button.btn.btn-clean.btn-sm.btn-icon.btn-icon-md")
    .first()
    .should("be.visible")
    .click({ force: true });
  cy.get("a.kt-nav__link").contains("Clone").click({ force: true });
  cy.wait(1500);
  cy.get("#title").clear();
  cy.get("#title").type(" Cloned");
  cy.get(
    "#web_link_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success"
  ).click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

// Add to Slider
Cypress.Commands.add("add_to_slider", () => {
  cy.get("#kt_switch_2").click({ force: true });
});

//  UPDATE STATUS UNPUBLISHED.
Cypress.Commands.add("update_status_unpublished", (name) => {
  cy.contains("h6", name, { matchCase: false })
    .last()
    .parents(".gallerybox-custom")
    .find(".gallery_checkbox")
    .check();
  cy.get("#kt_subheader_group_actions_status_change > .btn").click();
  cy.contains(".kt-nav__item a", "Unpublished").click();

  cy.get(".swal2-confirm").click();
  cy.reload();
  cy.wait(1500);
});

//  UPDATE STATUS PUBLISHED.

Cypress.Commands.add("update_status_published", (name) => {
  cy.contains("h6", name, { matchCase: false })
    .parents(".gallerybox-custom")
    .find(".gallery_checkbox")
    .check();
  cy.get("#kt_subheader_group_actions_status_change > .btn").click();
  cy.contains(".kt-nav__item a", "Published").click();

  cy.get(".swal2-confirm").click();
  cy.reload();
  cy.wait(1500);
});

// Dialogue Box Confirmation.
Cypress.Commands.add("yes", () => {
  cy.get(".swal2-confirm").should("be.visible").click({ force: true });
  cy.screenshot();
});

//****************************  NAVIGATION *****************************//

Cypress.Commands.add("open_Navigation", () => {
  cy.get(".kt-header__topbar-item--user > .kt-header__topbar-wrapper").click({
    force: true,
  });
  cy.get('[href="/navigation/"]').click({ force: true });
});

// ADD NAVIGATION

Cypress.Commands.add("add_Navigation", (name, nav_name) => {
  cy.get("#add_menu_navigation").should("be.visible").click();

  cy.get(
    '[style=""] > :nth-child(1) > :nth-child(1) > #kt_portlet_tools_4 > .kt-portlet__head > .kt-portlet__head-label > .w-100'
  ).click();

  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > :nth-child(1) > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > :nth-child(1) > .col-xl-8 > .row > .col > .form-control'
  )
    .last()
    .clear({ force: true })
    .then(($input) => {
      if (name !== undefined) {
        cy.wrap($input).type(name, { force: true });
      }
    })
    .last();
  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > :nth-child(1) > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > :nth-child(1) > .col-xl-8 > .dropdown > .btn'
  )
    .last()
    .click({ force: true });
  cy.get("a[role='option']").each(function ($ele) {
    if ($ele.text() === nav_name) {
      cy.log("found element");
      cy.wrap($ele).click({ force: true });
    }
  });
  cy.get("#kt_navigation_submit").click();
  cy.wait(7000);
});

//FIND NAVIGATION
Cypress.Commands.add("find_navigation", (name) => {
  cy.get("#kt_aside_mobile_toggler").click({ force: true });
  cy.get("#kt_aside_menu")
    .contains(name, { matchCase: false })
    .click({ force: true });
});
// **********************ADD ALBUM***********************************
Cypress.Commands.add("add_album", (name) => {
  cy.get("a > .btn").should("be.visible").click();

  cy.get("#album_name").type(name);
});
// SELECT ALBUM/
Cypress.Commands.add("select_album", (a_name) => {
  cy.contains("h6", a_name)
    .closest(".gallerybox-custom")
    .find(".gallery-img")
    .click();
});
// ADD PHOTO / Gallery
Cypress.Commands.add("add_gallery", (image_name, description, image) => {
  cy.get("a > .btn").click();
  cy.get('.form-control[name="name"]').type(image_name);
  cy.get(":nth-child(3) > .col-lg-10 > .form-control").type(description);
  cy.get("#kt_dropzone_1").attachFile(image, { subjectType: "drag-n-drop" });
});
// ADD Cover Photo
Cypress.Commands.add("add_Cover_photo", (image_name) => {
  cy.wait(2000);
  cy.contains("h6", image_name)
    .closest(".gallerybox-custom")
    .find(".cover_check")
    .check({ force: true });
});
//**************************EVENT****************************/

/// Add event
Cypress.Commands.add("add_event", (name, location, details, image) => {
  cy.get("a > .btn").should("be.visible").click();
  cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(name);

  cy.get("#kt_datetimepicker_3").click();

  cy.get(".day").contains("21").click({ force: true });
  cy.get(".hour.hour_pm").contains("4").click({ force: true });
  cy.get("fieldset.minute")
    .find("span.minute")
    .contains("4:15")
    .click({ force: true });

  //*********************************************************** */
  cy.get("#kt_datetimepicker_4").click({ force: true });
  cy.get("th.next").last().dblclick({ force: true });
  cy.get(
    ".datetimepicker-days > .table-condensed > tbody > :nth-child(5) > :nth-child(6)"
  )
    .last()
    .click();
  cy.get(
    ".datetimepicker-hours > .table-condensed > tbody > tr > td > :nth-child(2) > :nth-child(7)"
  )
    .last()
    .click();
  cy.get(
    ".datetimepicker-minutes > .table-condensed > tbody > tr > td > fieldset.minute > :nth-child(4)"
  )
    .last()
    .click();
  //***************************************************************** */
  cy.get("#address").type(location);
  cy.get(":nth-child(7) > .col-lg-10 > .form-control").select("UTC (0)");
  cy.get(":nth-child(8) > .col-lg-10 > .form-control").type(details);
  if (image) {
    cy.get("#kt_dropzone_1").attachFile(image, { subjectType: "drag-n-drop" });
  }
});

//************************** WEBLINKS ****************************/

Cypress.Commands.add("add_weblinks", (title, weblink) => {
  cy.contains("Add Link").click({ force: true });
  cy.wait(2500);

  cy.get("#title").type(title, { force: true });
  cy.wait(2500);

  cy.get("#link").type(weblink, { force: true });
  cy.get(
    "#web_link_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success"
  ).click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

//************************** SOCIAL MEDIA LINKS****************************/

Cypress.Commands.add("add_social_media_link", (name, link) => {
  cy.wait(2500);
  cy.get(".table_button_section > .btn-success")
    .should("be.visible")
    .click({ force: true });
  cy.get("#name")
    .select(name, { force: true })
    .should("have.value", name, { force: true });
  cy.get("#link").type(link, { force: true });
  cy.get(
    "#stay_connected_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success"
  ).click({ force: true });
  cy.screenshot();
  cy.wait(2000);
  cy.screenshot();
});

//************************** Legislative Bills ****************************/
Cypress.Commands.add(
  "add_legislative_bills",
  (
    bill_title,
    About_bill,
    Why_Is_This_Bill_Important,
    next_hearing,
    donation_link,
    description,
    send_email_to,
    image
  ) => {
    cy.get("a > .btn").should("be.visible").click();

    if (bill_title) {
      cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(bill_title);
    }
    if (About_bill) {
      cy.get(":nth-child(3) > .col-lg-10 > .form-control").type(About_bill);
    }
    if (Why_Is_This_Bill_Important) {
      cy.get(":nth-child(4) > .col-lg-10 > .form-control").type(
        Why_Is_This_Bill_Important
      );
    }
    if (next_hearing) {
      cy.get(":nth-child(5) > .col-lg-10 > .form-control").type(next_hearing);
    }
    if (donation_link) {
      cy.get(":nth-child(6) > .col-lg-10 > .form-control").type(donation_link);
    }
    if (description) {
      cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
        const $editable = $iframe.contents().find(".cke_editable");
        cy.wrap($editable).type(description);
      });
    }
    if (send_email_to) {
      cy.get(".tagify").type(send_email_to);
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    }
  }
);

//**************************** Multiple News *****************************/
Cypress.Commands.add(
  "add_multiple_news",
  (title, short_description, description, image) => {
    cy.get("a > .btn").should("be.visible").click();
    if (title) {
      cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(title);
    }
    if (short_description) {
      cy.get(":nth-child(3) > .col-lg-10 > .form-control").type(
        short_description
      );
    }
    if (description) {
      cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
        const $editable = $iframe.contents().find(".cke_editable");
        cy.wrap($editable).type(description);
      });
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    }
  }
);

//**************************** Union Representative *****************************//
Cypress.Commands.add(
  "add_unionrepresentaive",
  (
    name,
    designation,
    phone_1,
    phone_2,
    Fax,
    Email,
    address,
    website,
    description,
    image
  ) => {
    cy.get("a > .btn").should("be.visible").click();
    if (name) {
      cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(name);
    }
    if (designation) {
      cy.get(":nth-child(3) > .col-lg-10 > .form-control").type(designation);
    }
    if (phone_1) {
      cy.get(":nth-child(4) > .col-lg-10 > .form-control").type(phone_1);
    }
    if (phone_2) {
      cy.get(":nth-child(5) > .col-lg-10 > .form-control").type(phone_2);
    }
    if (Fax) {
      cy.get(":nth-child(6) > .col-lg-10 > .form-control").type(Fax);
    }
    if (Email) {
      cy.get(":nth-child(7) > .col-lg-10 > .form-control").type(Email);
    }
    if (address) {
      cy.get(":nth-child(8) > .col-lg-10 > .form-control").type(address);
    }
    if (website) {
      cy.get(":nth-child(9) > .col-lg-10 > .form-control").type(website);
    }
    if (description) {
      cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
        const $editable = $iframe.contents().find(".cke_editable");
        cy.wrap($editable).type(description);
      });
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    }
  }
);

//**************************** WEB VIEW TEST! *****************************/
Cypress.Commands.add("add_webview", (title, description, image) => {
  cy.get("a > .btn").should("be.visible").click();
  if (title) {
    cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(title);
  }
  if (description) {
    cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
      const $editable = $iframe.contents().find(".cke_editable");
      cy.wrap($editable).type(description);
    });
  }
  if (image) {
    cy.get("#kt_dropzone_1").attachFile(image, { subjectType: "drag-n-drop" });
  }
});

//************************** MEMBER DISCOUNT ****************************/

// ADD DISCOUNT BUTTON
Cypress.Commands.add("add_discount_type_button", () => {
  cy.get(".table_button_section > a > .btn").click();
});

// ADD DISCOUNT TYPE:
Cypress.Commands.add("add_discount_type", (name) => {
  cy.get(".add_discount_type").should("be.visible").click({ force: true });
  cy.get("#name").type(name, { force: true });
  cy.get("button.btn-success.submit").click({ force: true });
  cy.wait(2000);
});

//VIEW DISCOUNT/Documents BUTTON
Cypress.Commands.add("view_discount_button", () => {
  cy.get("a.btn-success").should("be.visible").click({ force: true });
});

// ADD DISCOUNT/Documents BUTTON
Cypress.Commands.add("add_discount_button", () => {
  cy.get(".kt-portlet__head-wrapper > a > .btn")
    .should("be.visible")
    .click({ force: true });
});

// ADD DISCOUNTS
Cypress.Commands.add(
  "add_discount",
  (name, type, website, short_description, description, image) => {
    if (name) {
      cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(name);
    }
    if (type) {
      cy.get(".select2-selection__rendered").click();
      cy.get(".select2-results__options").contains(type).click();
    }
    if (website) {
      cy.get(":nth-child(4) > .col-lg-10 > .form-control").type(website);
    }
    if (short_description) {
      cy.get(":nth-child(5) > .col-lg-10 > .form-control").type(
        short_description
      );
    }
    if (description) {
      cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
        const $editable = $iframe.contents().find(".cke_editable");
        cy.wrap($editable).type(description);
      });
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    }
  }
);

//*************************** MEMBER TOOLS ***********************************/
//open membertools
Cypress.Commands.add("open_Membertools_Navigation", () => {
  cy.get(".kt-header__topbar-item--user > .kt-header__topbar-wrapper")
    .should("be.visible")
    .click({ force: true });
  cy.get('[href="/member-tools-navigation/"]').click({ force: true });
});

// ADD MEMBER TOOLS Navigation
Cypress.Commands.add("add_membertools", (name, nav_name) => {
  cy.wait(1500);
  cy.get("#add_menu_navigation").click();
  cy.get(
    '[style=""] > :nth-child(1) > :nth-child(1) > #kt_portlet_tools_4 > .kt-portlet__head > .kt-portlet__head-label > .w-100'
  ).click();
  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > :nth-child(1) > .col-lg-8 > .row > .col > .form-control'
  ).clear();
  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > :nth-child(1) > .col-lg-8 > .row > .col > .form-control'
  ).type(name);
  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > :nth-child(1) > .col-lg-8 > .dropdown > .btn'
  ).click({ force: true });
  cy.get("a[role='option']").each(function ($ele) {
    if ($ele.text() === nav_name) {
      cy.log("found element");
      cy.wrap($ele).click();
    }
  });
  cy.get("#kt_navigation_submit").click();
  cy.wait(7000);
});

//**************************** Member tools Union Representative *****************************//
Cypress.Commands.add(
  "add_membertools_unionrepresentaive",
  (
    name,
    designation,
    phone_1,
    phone_2,
    Fax,
    Email,
    industry,
    address,
    website,
    description,
    image
  ) => {
    cy.get("a > .btn").should("be.visible").click();
    if (name) {
      cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(name);
    }
    if (designation) {
      cy.get(":nth-child(3) > .col-lg-10 > .form-control").type(designation);
    }
    if (phone_1) {
      cy.get(":nth-child(4) > .col-lg-10 > .form-control").type(phone_1);
    }
    if (phone_2) {
      cy.get(":nth-child(5) > .col-lg-10 > .form-control").type(phone_2);
    }
    if (Fax) {
      cy.get(":nth-child(6) > .col-lg-10 > .form-control").type(Fax);
    }
    if (Email) {
      cy.get(":nth-child(7) > .col-lg-10 > .form-control").type(Email);
    }
    if (industry) {
      cy.get(
        ":nth-child(8) > .col-lg-10 > .dropdown > .dropdown-toggle"
      ).click();
      cy.get("a.dropdown-item").contains(industry).click();
    }
    if (address) {
      cy.get(":nth-child(9) > .col-lg-10 > .form-control").type(address, {
        force: true,
      });
    }
    if (website) {
      cy.get(":nth-child(10) > .col-lg-10 > .form-control").type(website);
    }

    if (description) {
      cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
        const $editable = $iframe.contents().find(".cke_editable");
        cy.wrap($editable).type(description);
      });
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    }
  }
);

//**************************** Member Doccuments *****************************//
// Add Document
Cypress.Commands.add("add_document_type", (name) => {
  cy.get(".add_document_type").should("be.visible").click({ force: true });
  cy.wait(1500);

  cy.get("#name").type(name, { force: true });
  cy.get(
    "#document_type_modal > .modal-dialog > .modal-content > .modal-footer > .btn-success"
  ).click({ force: true });
  cy.wait(2000);
});

// Add DOCUMENT BUTTON
Cypress.Commands.add("add_document_button", () => {
  cy.get(".kt-portlet__head-wrapper > .btn")
    .should("be.visible")
    .click({ force: true });
});

// ADD Documents
Cypress.Commands.add(
  "add_document",
  (name, type, industry, website, short_description, description, image) => {
    if (name) {
      cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(name);
    }
    if (type) {
      cy.get(
        ":nth-child(3) > .col-lg-10 > .dropdown > .dropdown-toggle"
      ).click();
      cy.get("a.dropdown-item").contains(type).click();
    }
    if (industry) {
      cy.get(":nth-child(4) > .col-lg-10 > .dropdown > .dropdown-toggle").click(
        { force: true }
      );
      cy.get("a.dropdown-item").contains(industry).click();
    }
    if (website) {
      cy.get(":nth-child(5) > .col-lg-10 > .form-control").type(website, {
        force: true,
      });
    }
    if (short_description) {
      cy.get(":nth-child(6) > .col-lg-10 > .form-control").type(
        short_description
      );
    }
    if (description) {
      cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
        const $editable = $iframe.contents().find(".cke_editable");
        cy.wrap($editable).type(description);
      });
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    }
  }
);
//**************************** Industry News & Events*****************************/

Cypress.Commands.add(
  "add_industry_news",
  (title, short_description, industry, description, image) => {
    cy.get("a > .btn").should("be.visible").click();
    if (title) {
      cy.get(":nth-child(2) > .col-lg-10 > .form-control").type(title);
    }
    if (short_description) {
      cy.get(":nth-child(3) > .col-lg-10 > .form-control").type(
        short_description
      );
    }
    if (industry) {
      cy.get(
        ":nth-child(4) > .col-lg-10 > .dropdown > .dropdown-toggle"
      ).click();
      cy.get("a.dropdown-item").contains(industry).click();
      cy.get(
        ":nth-child(4) > .col-lg-10 > .dropdown > .dropdown-toggle"
      ).click();
    }
    //  cy.get(':nth-child(4) > .col-lg-10 > .dropdown > .dropdown-toggle').click()
    //  cy.get('.bs-select-all').click()
    // cy.get(':nth-child(4) > .col-lg-10 > .dropdown > .dropdown-toggle').click()
    if (description) {
      cy.get("iframe.cke_wysiwyg_frame").then(($iframe) => {
        const $editable = $iframe.contents().find(".cke_editable");
        cy.wrap($editable).type(description);
      });
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    }
  }
);

//**************************** PUSH NOTIFICATIONS *****************************/

Cypress.Commands.add("open_Notifications", () => {
  cy.get(".kt-header__topbar-item--user > .kt-header__topbar-wrapper").click();
  cy.get('[href="/push-notification/send/"]').click();
});

// Fill Notification data.
Cypress.Commands.add(
  "Fill_Notification",
  (zip, URL, post_index, image, title, message) => {
    if (zip) {
      cy.get(
        '.dropdown.bootstrap-select.show-tick.form-control.kt- select[name="zip[]"]'
      ).select(zip, { force: true });
    }
    cy.get(".bootstrap-switch-label").click();
    if (URL) {
      cy.get("input.form-control.custom_url").type(URL, { force: true });
    }
    if (post_index) {
      cy.get("button.btn.dropdown-toggle.btn-light")
        .last()
        .click({ force: true });
      cy.get(".optgroup-1").find("a.opt").eq(post_index).click();
    }
    if (image) {
      cy.get("#kt_dropzone_1").attachFile(image, {
        subjectType: "drag-n-drop",
      });
    } else {
      cy.get(".kt-checkbox").click();
    }

    if (title) {
      cy.get('input.form-control.input[name="title"]').type(title);
    }
    if (message) {
      cy.get('textarea.form-control.kt-resize[name="message"]').type(message);
    }
  }
);

// Send Notification button
Cypress.Commands.add("send_notification_button", () => {
  cy.get(".kt-portlet__head-wrapper > .btn-success").click({ force: true });
  cy.get(
    "#sent-popup > .modal-dialog > .modal-content > .modal-footer > .btn-success"
  )
    .should("be.visible")
    .click({ force: true });
});

// Send Push

Cypress.Commands.add("send_push_button", () => {
  cy.get(".kt-portlet__head-wrapper > .btn").should("be.visible").click();
});

// Registered Members

Cypress.Commands.add("Registered_members", () => {
  cy.get('input.push_type[data-type="RegisterdUsers"][value="2"]').check({
    force: true,
  });
});

// UnRegistered Members

Cypress.Commands.add("Unregistered_members", () => {
  cy.get('input.push_type[data-type="UnregisterdUsers"][value="2"]').check({
    force: true,
  });
});

//Intelligent Delivery

Cypress.Commands.add("Intelligent_delivery", () => {
  cy.get('input[type="radio"][name="optimization"][value="2"]').check({
    force: true,
  });
});

//Schedule Notifications

Cypress.Commands.add("Schedule_Notification", () => {
  cy.get(
    ".delivery-section > .col-lg-8 > .kt-radio-list > :nth-child(2) > span"
  ).click();
  cy.get("#today_date").click({ force: true });
  cy.get("td.day.today.active").click();
  cy.get(
    ".datetimepicker-hours > .table-condensed > tbody > tr > td > .active"
  ).click({force: true});
  cy.get('td[colspan="7"]')
    .find("span.minute.active")
    .next("span.minute")
    .click();
});

//////////////////////////

//****************************  INFORMATION SETTINGS.*****************************/

// Open Info NAVIGATION

Cypress.Commands.add("open_InformationSettings", () => {
  cy.get(".kt-header__topbar-item--user > .kt-header__topbar-wrapper").click();
  cy.get('[href="/info-settings/"]').click();
});

// ADD Info NAVIGATIONS

Cypress.Commands.add("add_Info_Navigation", (name, nav_name, link) => {
  cy.get("#add_menu_navigation").click();
  cy.get(
    '[style=""] > :nth-child(1) > :nth-child(1) > #kt_portlet_tools_4 > .kt-portlet__head > .kt-portlet__head-label > .w-100'
  ).click();
  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > :nth-child(1) > .col-lg-8 > .row > .col > .form-control'
  ).clear({ force: true });
  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(1) > :nth-child(1) > .col-lg-8 > .row > .col > .form-control'
  ).type(name);
  cy.get(
    '[data-repeater-item=""][style=""] > :nth-child(1) > .col-lg-12 > #kt_portlet_tools_4 > .kt-portlet__body > .kt-portlet__content > :nth-child(1) > :nth-child(2) > .form-group > .col-lg-8 > .dropdown > .btn'
  ).click();
  cy.get("a[role='option']").each(function ($ele, index, list) {
    if ($ele.text() === nav_name) {
      cy.log("found element");
      cy.wrap($ele).click();
    }
  });
  if (link) {
    cy.get('input.form-control[placeholder="Enter Web Link"]')
      .last()
      .type(link);
  } else {
    cy.log("No link provided");
  }
  cy.get("#kt_navigation_submit").should("be.visible").click();
  cy.wait(5000);
});

/*****************************************************************/
Cypress.Commands.add("customcheckAlly", () => {
  function callback(violations) {}
  cy.checkA11y(null, null, callback);
});
