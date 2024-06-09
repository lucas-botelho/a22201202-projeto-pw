import os
import subprocess

def djangoAppInit(app_name):

    command = f'python manage.py startapp {app_name}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.path.abspath("./"))

    if result.returncode == 0:
        pySettings = os.path.abspath("./project/settings.py")
        with open(pySettings) as settingsFile:
            lines = settingsFile.readlines()

        isInInstalledApps = False
        for line in lines:
            if line.__contains__("INSTALLED_APPS"):
                isInInstalledApps = True
            
            if line.__eq__(']\n') and isInInstalledApps:
                lines.insert(lines.index(line), "    '" + app_name + "',\n" )
                break
        
        with open(pySettings, 'w') as file:
            file.writelines(lines)

        newProjectPath = os.path.abspath(f'./{app_name}')

        with open(f'{newProjectPath}/urls.py', 'w') as file:
            content = "from django.urls import path\nfrom . import views\n\nurlpatterns = [\n   \n]"
            file.write(content)

        projectUrls = os.path.abspath("./project/urls.py")

        with open(projectUrls, 'r+') as file:
            lines = file.readlines()
            new_line = f"    path('{app_name}/', include('{app_name}.urls')),\n"
            lines.insert(-1, new_line)
            file.seek(0)
            file.writelines(lines)
    else:
            print(result.stderr)


djangoAppInit(app_name=input("new app name="))

