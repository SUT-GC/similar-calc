CREATE SEQUENCE "public"."dom_baidu_restairamt_info_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;

DROP TABLE IF EXISTS "public"."dom_baidu_restairamt_info";
CREATE TABLE "public"."dom_baidu_restairamt_info" (
    "id" int8 NOT NULL DEFAULT nextval('dom_baidu_restairamt_info_seq'::regclass),
    "baidu_id" int8 NOT NULL DEFAULT 0,
    "baidu_name" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "baidu_branch_name" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "baidu_address" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "baidu_phone" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "baidu_latitude" numeric NOT NULL DEFAULT 0.0,
    "baidu_longitude" numeric NOT NULL DEFAULT 0.0,
    "baidu_logo_hash" varchar(512) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "baidu_is_value" int2 NOT NULL DEFAULT 0,
    "created_at" timestamp(6) NOT NULL DEFAULT now(),
    "updated_at" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."dom_baidu_restairamt_info" OWNER TO "postgres";

ALTER TABLE "public"."dom_baidu_restairamt_info" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "public"."dom_baidu_restairamt_info_seq" OWNER TO "postgres";

CREATE INDEX  "ix_baidu_id" ON "public"."dom_baidu_restairamt_info" USING btree(baidu_id ASC NULLS LAST);
CREATE INDEX  "ix_baidu_name" ON "public"."dom_baidu_restairamt_info" USING btree(baidu_name ASC NULLS LAST);
CREATE INDEX  "ix_baidu_branch_name" ON "public"."dom_baidu_restairamt_info" USING btree(baidu_branch_name ASC NULLS LAST);
CREATE INDEX  "ix_baidu_phone" ON "public"."dom_baidu_restairamt_info" USING btree(baidu_phone ASC NULLS LAST);
CREATE INDEX  "ix_baidu_address" ON "public"."dom_baidu_restairamt_info" USING btree(baidu_address ASC NULLS LAST);
