CREATE TABLE "public.Employee" (
	"id" serial NOT NULL,
	"name" TEXT NOT NULL,
	"surname" TEXT NOT NULL,
	"date_of_birth" DATE NOT NULL,
	"title_id" integer NOT NULL,
	CONSTRAINT "Employee_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);


CREATE TABLE "public.Title" (
	"id" serial NOT NULL,
	"title_name" VARCHAR(255) NOT NULL,
	CONSTRAINT "Title_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.team" (
	"id" serial NOT NULL,
	"team_name" VARCHAR(255) NOT NULL,
	"employee_id" integer NOT NULL,
	"product_id" integer NOT NULL,
	CONSTRAINT "team_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Product" (
	"id" serial NOT NULL,
	"product_name" VARCHAR(255) NOT NULL,
	"owner_id" integer NOT NULL,
	CONSTRAINT "Product_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.owner" (
	"id" serial NOT NULL,
	"name" TEXT NOT NULL,
	CONSTRAINT "owner_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.owner_domain" (
	"id" serial NOT NULL,
	"owner_id" integer NOT NULL,
	"product_id" integer NOT NULL,
	"domain_id" integer NOT NULL,
	CONSTRAINT "owner_domain_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.domain" (
	"id" serial NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	CONSTRAINT "domain_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "public.Employee" ADD CONSTRAINT "Employee_fk0" FOREIGN KEY ("title_id") REFERENCES "public.Title"("id");

ALTER TABLE "public.team" ADD CONSTRAINT "team_fk0" FOREIGN KEY ("employee_id") REFERENCES "public.Employee"("id");
ALTER TABLE "public.team" ADD CONSTRAINT "team_fk1" FOREIGN KEY ("product_id") REFERENCES "public.Product"("id");

ALTER TABLE "public.Product" ADD CONSTRAINT "Product_fk0" FOREIGN KEY ("owner_id") REFERENCES "public.owner"("id");


ALTER TABLE "public.owner_domain" ADD CONSTRAINT "owner_domain_fk0" FOREIGN KEY ("owner_id") REFERENCES "public.owner"("id");
ALTER TABLE "public.owner_domain" ADD CONSTRAINT "owner_domain_fk1" FOREIGN KEY ("product_id") REFERENCES "public.Product"("id");
ALTER TABLE "public.owner_domain" ADD CONSTRAINT "owner_domain_fk2" FOREIGN KEY ("domain_id") REFERENCES "public.domain"("id");









