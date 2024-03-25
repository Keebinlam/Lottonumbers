import webbrowser

def open_urls(urls):
    for url in urls:
        webbrowser.open(url)

if __name__ == "__main__":
    urls = [
        "https://adobe.gainsightcloud.com/v1/ui/dashboard#/c17936c0-cf3c-46c1-9326-50ce39d55a77",
        "https://app.powerbi.com/groups/me/apps/0b6e808d-1da1-4708-99ae-ca0940ac066d/reports/751d939d-54c3-43ec-881e-555395581821/ReportSection0f26e45e4a254683a70c?chromeless=1&experience=power-bi"
    ]
    open_urls(urls)
#pyinstaller. —name Davidapp —oneline —windowless — icon=icon.ico Davidapp.py

import webbrowser

def open_urls(urls):
    for url in urls:
        webbrowser.open(url)

if __name__ == "__main__":
    urls = [
        "https://adobe.gainsightcloud.com/v1/ui/dashboard#/d7930d93-168e-4148-85aa-4dcd4d3b34ff",
        "https://app.powerbi.com/groups/me/apps/0b6e808d-1da1-4708-99ae-ca0940ac066d/reports/751d939d-54c3-43ec-881e-555395581821/ReportSection0f26e45e4a254683a70c?chromeless=1&experience=power-bi",
        "https://workfront.lightning.force.com/lightning/r/Dashboard/01Z4X000001XPyMUAW/view?queryScope=userFolders"
    ]
    open_urls(urls)

#pyinstaller. —name Steveapp —oneline —windowless — icon=icon.ico Steveapp.py