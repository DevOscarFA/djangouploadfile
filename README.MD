## Ingresar a postgres
sudo -u postgres psql

# Consultar las base de datos
SELECT datname FROM pg_database WHERE datistemplate = false;

# Auto rename file upload with file validator
https://djangosnippets.org/snippets/10565/