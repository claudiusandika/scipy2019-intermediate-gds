import importlib

packages = ['geopandas', 'sklearn', 'contextily', 'rasterio', 'libpysal',
            'rasterstats', 'geopy']

bad = []
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        bad.append("Can't import %s" % package)
else:
    if len(bad) > 0:
        print('Your tutorial environment is not yet fully set up:')
        print('\n'.join(bad))
    else:
        try:
            import geopandas
            countries = geopandas.read_file("zip://./data/ne_110m_admin_0_countries.zip")
            print("All good. Enjoy the tutorial!")
        except Exception as e:
            print("Couldn't read countries shapefile.")
            print(e)

