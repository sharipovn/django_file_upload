CREATE USER file_upload WITH PASSWORD 'file_upload';
GRANT ALL PRIVILEGES ON DATABASE reestr TO file_upload;
ALTER USER file_upload SET search_path = file_upload;


