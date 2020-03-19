# coding: utf-8
#!/usr/bin/env python3

import os
import io

# The actual path
path = os.getcwd()

# Input to type the project name and title
projectName = raw_input('Enter the project name: ')
projectTitle = raw_input('Enter the project title: ')

# Project folders
projectMainFolder = path + '/' + projectName
projectAssetsFolder = projectMainFolder + '/assets/'
projectStylesFolder = projectAssetsFolder + '/css/'
projectScriptsFolder = projectAssetsFolder + '/js/'
projectImagesFolder = projectAssetsFolder + '/img/'

try:
    # Creating project folders
    os.mkdir(projectMainFolder)
    os.mkdir(projectAssetsFolder)
    os.mkdir(projectScriptsFolder)
    os.mkdir(projectStylesFolder)
    os.mkdir(projectImagesFolder)

    # Create the main files and open it to insert a template
    # indexFile = open(projectMainFolder + '/index.html', 'w+')

    cssFile = open(projectStylesFolder + '/main.css', 'w+')
    jsFile = open(projectScriptsFolder + '/main.js', 'w+')

    # Writting HTML template
    with io.open(projectMainFolder + '/index.html', 'wb') as indexFile:
        indexFile.write('<!DOCTYPE html>\n')
        indexFile.write('<html lang="en">\n')
        indexFile.write('<head>\n')
        indexFile.write('  <meta charset="UTF-8">\n')
        indexFile.write('  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">\n')
        indexFile.write('  <title>%s</title>\n\n' % projectTitle)
        indexFile.write('  <!-- Main CSS -->\n')
        indexFile.write('  <link rel="stylesheet" href="./assets/css/main.css">\n')
        indexFile.write('</head>\n')
        indexFile.write('<body>\n')
        indexFile.write('  <h1 class="main-title">%s</h1>\n\n' % projectTitle)
        indexFile.write('  <!-- Main Script -->\n')
        indexFile.write('  <script src="./assets/js/main.js"></script>\n')
        indexFile.write('</body>\n')
        indexFile.write('</html>\n')

    # Writting CSS template
    cssFile.write('// Clear body default style\n')
    cssFile.write('body {\n')
    cssFile.write('  margin: 0;\n')
    cssFile.write('  padding: 0;\n')
    cssFile.write('  box-sizing: border-box;\n')
    cssFile.write('}\n\n')
    cssFile.write('.main-title {\n')
    cssFile.write('  color: blue;\n')
    cssFile.write('  width: 100%;\n')
    cssFile.write('  font-family: "Helvetica", "Arial", "Verdana", sans-serif;\n')
    cssFile.write('  text-align: center;\n')
    cssFile.write('  padding: 10px;\n')
    cssFile.write('}')

    # Close both index and css file
    indexFile.close()
    cssFile.close()

except OSError:
    print ('Creation of the project %s failed' % projectName)
else:
    print ('Successfully created the project %s ' % projectName)

