exports.config =
  files:
    javascripts:
      joinTo:
        '../../nedviga_backend/static/javascripts/frontend_docs_code.js': /^app/
        '../../nedviga_backend/static/javascripts/frontend_docs_vendor.js': /^(?!app)/

    stylesheets:
      joinTo: '../../nedviga_backend/static/stylesheets/frontend_docs.css'

  paths:
    'public': '../nedviga_backend/static'