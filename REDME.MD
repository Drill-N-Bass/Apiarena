Start of work.

At this stage, the old `ultiglobal.com` website was downloaded from the internet using the` HTTrack` application. Then I added all the static files from the old site to the project in Django ("Apiarena Django site"). This is how the work on the new website `apiarena.com` began.

After adding the appropriate paths to `settings.py`:
``
STATIC_URL = '/ static /'
STATICFILES_DIRS = [os.path.join (BASE_DIR, 'static'),]
``
and a `html` file named` home.html` to `/ Templates`, I modified the import paths of the` js` libraries.

For this, I changed link from `../` to `https: //`