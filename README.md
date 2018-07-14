# Flask Babel Bundle

Adds support for translations to Flask Unchained


# usage for bundle-specific translations

### babel.cfg
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

translation keys must be in the format of `<bundle_pkg_name>.some.unique.identifier` and `<bundle_pkg_name>.some.unique.identifier.plural` for pluralizable strings

## first, extract strings
```
pybabel extract -F babel.cfg -o <bundle_pkg_name>/translations/<bundle_pkg_name>.pot .
```

## second, init a language (only required the first time)
```
pybabel init -i <bundle_pkg_name>/translations/<bundle_pkg_name>.pot -d <bundle_pkg_name>/translations -l <language_code>
```

## third, compile the translations
```
pybabel compile -d <bundle_pkg_name>/translations -D <bundle_pkg_name>
```


# usage from app bundle

use the messages domain via helper commands:

* flask babel extract
* flask babel init <lang_code>
* flask babel compile
