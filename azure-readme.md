This app was created using the Blogpost mentioned in the README

However it won't work as it on Azure App Service. 

Changes to sample app to get it to run on Azure
---


1. "App Service looks for a file named application.py or app.py" 
    1. added an app.py which seems to work 
    1. could also create a custom startup command (e.g. app is simply "blog")
    
2. Installing requirements (pip install...)
    1. The App Service deployment engine automatically activates a virtual environment and runs pip install -r requirements.txt for you when you deploy a Git repository, or a Zip package with build processes switched on.
    2. this code originally just had a setup.py, I added a requirements.txt based on that


3. database
    1. the readme doesn't say this, but I couldn' run the app until I ran `flask init-db`
    1. not sure how we will get that command as part of the deploy but perhaps post-build command

4. gitignore - keep the actual config files out of git!

Configurating for Azure deployment
.     
1. App URL
    1. the blog post has good examples for using localhost:5000, but this won't work for Azure
    1. pick an name for your app - this must be unique across all of azure.  Perhaps use your netid
    1. default URL for azure is http://<appname>.azurewebsites.net
    1. Okta apps require this URL in the okta dashboard setup.  In the blog post where they have you enter
    1. as well as config file client_secrets.json for the redirect URLs

For example the app name "ads-oktablogtest"

1. goto to the Okta dashboard and log-in
2. click applications to list your applications
3. click your app, then the 'general tab' which list the config
4. click the 'edit' button and change the following : 

    ```bash
    LOGIN
    Login redirect URIs : (click add url)        
        http://<appname>.azurewebsites.net/oidc/callback	
    
    Logout redirect URIs : (click add url)
        http://<appname>.azurewebsites.net	

    Login initiated by  
    App Only
    Initiate login URI  (edit this url to Azure , not sure what else to put  )
        http://<appname>.azurewebsites.net/oidc/callback
    ```   

You shouldn't have to recreate the app id/secret values that you used to test for localhost.  

Not sure the easiest way to create this app from the portal. 

the Az command line (requires installation of the Azure cli in your favorite version of python)   

```bash
az webapp up --sku D1 -g <your_resource_group> -n <app-name>
```

for example: 

```bash
az webapp up --sku D1 -g ads-billspat-testing-rg -n ads-oktablogtest
```
