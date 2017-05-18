CREATE SEQUENCE "public"."dom_restaurant_not_relation_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;

DROP TABLE IF EXISTS "public"."dom_restaurant_not_relation";
CREATE TABLE "public"."dom_restaurant_not_relation" (
    "id" int8 NOT NULL DEFAULT nextval('dom_restaurant_not_relation_seq'::regclass),
    "eleme_poi_id" int8 NOT NULL DEFAULT 0,
    "other_poi_id" int8 NOT NULL DEFAULT 0,
    "source" int2 NOT NULL DEFAULT 0,
    "is_valid" int2 NOT NULL DEFAULT 0,
    "created_at" timestamp(6) NOT NULL DEFAULT now(),
    "updated_at" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."dom_restaurant_not_relation" OWNER TO "postgres";

ALTER TABLE "public"."dom_restaurant_not_relation" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "public"."dom_restaurant_not_relation_seq" OWNER TO "postgres";

CREATE INDEX  "ix_not_eleme_poi_id" ON "public"."dom_restaurant_not_relation" USING btree(eleme_poi_id ASC NULLS LAST);
CREATE INDEX  "ix_not_other_poi_id" ON "public"."dom_restaurant_not_relation" USING btree(other_poi_id ASC NULLS LAST);
CREATE INDEX  "ix_not_source" ON "public"."dom_restaurant_not_relation" USING btree(source ASC NULLS LAST);