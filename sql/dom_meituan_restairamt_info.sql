CREATE SEQUENCE "public"."dom_meituan_restairamt_info_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;

DROP TABLE IF EXISTS "public"."dom_meituan_restairamt_info";
CREATE TABLE "public"."dom_meituan_restairamt_info" (
    "id" int8 NOT NULL DEFAULT nextval('dom_meituan_restairamt_info_seq'::regclass),
    "meituan_id" int8 NOT NULL DEFAULT 0,
    "meituan_name" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "meituan_branch_name" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "meituan_address" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "meituan_phone" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "meituan_latitude" numeric NOT NULL DEFAULT 0.0,
    "meituan_longitude" numeric NOT NULL DEFAULT 0.0,
    "meituan_logo_hash" varchar(512) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "meituan_is_value" int2 NOT NULL DEFAULT 0,
    "created_at" timestamp(6) NOT NULL DEFAULT now(),
    "updated_at" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."dom_meituan_restairamt_info" OWNER TO "postgres";

ALTER TABLE "public"."dom_meituan_restairamt_info" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "public"."dom_meituan_restairamt_info_seq" OWNER TO "postgres";

CREATE INDEX  "ix_meituan_id" ON "public"."dom_meituan_restairamt_info" USING btree(meituan_id ASC NULLS LAST);
CREATE INDEX  "ix_meituan_name" ON "public"."dom_meituan_restairamt_info" USING btree(meituan_name ASC NULLS LAST);
CREATE INDEX  "ix_meituan_branch_name" ON "public"."dom_meituan_restairamt_info" USING btree(meituan_branch_name ASC NULLS LAST);
CREATE INDEX  "ix_meituan_phone" ON "public"."dom_meituan_restairamt_info" USING btree(meituan_phone ASC NULLS LAST);
CREATE INDEX  "ix_meituan_address" ON "public"."dom_meituan_restairamt_info" USING btree(meituan_address ASC NULLS LAST);
