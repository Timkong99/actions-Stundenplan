import requests
from icalendar import Calendar, Event

if __name__ == '__main__':
    r = requests.get('https://vorlesungsplan.nicolaikobras.de/calendars/SD_2021_1.ics')

    cal = Calendar.from_ical(r.content)

    for component in cal.walk():
        if component.name == 'VEVENT':
            if component.get('summary') == 'Requirements Engineering und Usability SD Vorlesung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Requirements Engineering und Usability SD Übung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Programmiertechnik III SD Vorlesung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Programmiertechnik III SD Übung':
                cal.subcomponents.remove(component)

    f = open('out/SD_2021_1.ics', 'wb')
    f.write(cal.to_ical())
    f.close()

    r = requests.get('https://vorlesungsplan.nicolaikobras.de/calendars/SD_2022_1.ics')

    cal = Calendar.from_ical(r.content)
    
    for component in cal.walk():
        if component.name == 'VEVENT':
            if component.get('summary') == 'Multimediatechnologie SD Vorlesung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Mathematik I SD Vorlesung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Programmiertechnik I SD Vorlesung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Tutorium Mathematik I SD Tutorium':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Mathematik I SD Übung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Multimediatechnologie SD Übung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Programmiertechnik I SD Übung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Grundlagen der IT Hardware SD Übung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Grundlagen der IT Hardware SD Vorlesung':
                cal.subcomponents.remove(component)
            if component.get('summary') == 'Tutorium Programmiertechnik I + II SD Tutorium':
                cal.subcomponents.remove(component)

    f = open('out/SD_2022_1.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
