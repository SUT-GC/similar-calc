CREATE SEQUENCE "public"."dom_eleme_restaurant_info_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;

DROP TABLE IF EXISTS "public"."dom_eleme_restaurant_info";
CREATE TABLE "public"."dom_eleme_restaurant_info" (
    "id" int8 NOT NULL DEFAULT nextval('dom_eleme_restaurant_info_seq'::regclass),
    "eleme_id" int8 NOT NULL DEFAULT 0,
    "eleme_name" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "eleme_branch_name" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "eleme_address" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "eleme_phone" varchar(255) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "eleme_latitude" numeric NOT NULL DEFAULT 0.0,
    "eleme_longitude" numeric NOT NULL DEFAULT 0.0,
    "eleme_logo_hash" varchar(512) NOT NULL DEFAULT ''::character varying COLLATE "default",
    "eleme_is_value" int2 NOT NULL DEFAULT 0,
    "created_at" timestamp(6) NOT NULL DEFAULT now(),
    "updated_at" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."dom_eleme_restaurant_info" OWNER TO "postgres";

ALTER TABLE "public"."dom_eleme_restaurant_info" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "public"."dom_eleme_restaurant_info_seq" OWNER TO "postgres";

CREATE INDEX  "ix_eleme_id" ON "public"."dom_eleme_restaurant_info" USING btree(eleme_id ASC NULLS LAST);
CREATE INDEX  "ix_eleme_name" ON "public"."dom_eleme_restaurant_info" USING btree(eleme_name ASC NULLS LAST);
CREATE INDEX  "ix_eleme_branch_name" ON "public"."dom_eleme_restaurant_info" USING btree(eleme_branch_name ASC NULLS LAST);
CREATE INDEX  "ix_eleme_phone" ON "public"."dom_eleme_restaurant_info" USING btree(eleme_phone ASC NULLS LAST);
CREATE INDEX  "ix_eleme_address" ON "public"."dom_eleme_restaurant_info" USING btree(eleme_address ASC NULLS LAST);
