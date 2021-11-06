SELECT PG_ENCODING_TO_CHAR("encid") AS "Charset", '' AS "Description" FROM (SELECT "conforencoding" AS "encid" FROM "pg_conversion", "pg_database" WHERE "contoencoding"="encoding" AND "datname"=CURRENT_DATABASE()) AS "e";

SELECT "p"."proname", "p"."proargtypes" FROM "pg_catalog"."pg_namespace" AS "n" JOIN "pg_catalog"."pg_proc" AS "p" ON "p"."pronamespace" = "n"."oid" WHERE "n"."nspname"='letscode';

SELECT "nspname" FROM "pg_catalog"."pg_namespace" ORDER BY "nspname";

SELECT "p"."proname", "p"."proargtypes" FROM "pg_catalog"."pg_namespace" AS "n" JOIN "pg_catalog"."pg_proc" AS "p" ON "p"."pronamespace" = "n"."oid" WHERE "n"."nspname"='letscode';


 SELECT datname FROM pg_database WHERE datistemplate=FALSE;


 SELECT NOW() + INTERVAL '10 MINUTE';


 CREATE DATABASE northwind
    WITH 
    OWNER = letscode
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;