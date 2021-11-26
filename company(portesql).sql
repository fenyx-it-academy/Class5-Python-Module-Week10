CREATE TABLE "public.Employee" (
	"Employee_id" serial NOT NULL,
	"name" serial NOT NULL,
	"title" serial NOT NULL,
	CONSTRAINT "Employee_pk" PRIMARY KEY ("Employee_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Title" (
	"Title_id" serial NOT NULL,
	"Title_name" serial NOT NULL,
	CONSTRAINT "Title_pk" PRIMARY KEY ("Title_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Products" (
	"Product_id" serial NOT NULL,
	"Product_name" serial NOT NULL,
	"price" serial NOT NULL,
	CONSTRAINT "Products_pk" PRIMARY KEY ("Product_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Team" (
	"Team_id" serial NOT NULL,
	"Team_name" serial NOT NULL,
	"employee" serial NOT NULL,
	"product" serial NOT NULL,
	CONSTRAINT "Team_pk" PRIMARY KEY ("Team_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Customer" (
	"customer_id" serial NOT NULL,
	"customer_name" serial NOT NULL,
	"customer_adress" serial NOT NULL,
	"product" serial NOT NULL,
	CONSTRAINT "Customer_pk" PRIMARY KEY ("customer_id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "Employee" ADD CONSTRAINT "Employee_fk0" FOREIGN KEY ("title") REFERENCES "Title"("Title_id");



ALTER TABLE "Team" ADD CONSTRAINT "Team_fk0" FOREIGN KEY ("employee") REFERENCES "Employee"("Employee_id");
ALTER TABLE "Team" ADD CONSTRAINT "Team_fk1" FOREIGN KEY ("product") REFERENCES "Products"("Product_id");

ALTER TABLE "Customer" ADD CONSTRAINT "Customer_fk0" FOREIGN KEY ("product") REFERENCES "Products"("Product_id");






