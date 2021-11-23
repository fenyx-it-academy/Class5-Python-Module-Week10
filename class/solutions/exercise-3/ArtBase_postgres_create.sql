CREATE TABLE "public.Artist" (
	"name" TEXT NOT NULL,
	"birthplace" TEXT NOT NULL,
	"age" integer NOT NULL,
	"style" TEXT NOT NULL,
	CONSTRAINT "Artist_pk" PRIMARY KEY ("name")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Artwork" (
	"title" TEXT NOT NULL,
	"artist" TEXT NOT NULL,
	"year" integer NOT NULL,
	"art" TEXT NOT NULL,
	"price" integer NOT NULL,
	CONSTRAINT "Artwork_pk" PRIMARY KEY ("title")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Group" (
	"name" TEXT NOT NULL,
	CONSTRAINT "Group_pk" PRIMARY KEY ("name")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Customer" (
	"name" TEXT NOT NULL,
	"adress" TEXT NOT NULL,
	"amount" integer NOT NULL,
	CONSTRAINT "Customer_pk" PRIMARY KEY ("name")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Artwork_Group" (
	"artwork_title" TEXT NOT NULL,
	"group_name" TEXT NOT NULL,
	CONSTRAINT "Artwork_Group_pk" PRIMARY KEY ("artwork_title","group_name")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Customer_Group" (
	"customer_name" TEXT NOT NULL,
	"group_name" TEXT NOT NULL,
	CONSTRAINT "Customer_Group_pk" PRIMARY KEY ("customer_name","group_name")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Customer_Artist" (
	"artist_name" TEXT NOT NULL,
	"customer_name" TEXT NOT NULL,
	CONSTRAINT "Customer_Artist_pk" PRIMARY KEY ("artist_name","customer_name")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "public.Artwork" ADD CONSTRAINT "Artwork_fk0" FOREIGN KEY ("artist") REFERENCES "public.Artist"("name");



ALTER TABLE "public.Artwork_Group" ADD CONSTRAINT "Artwork_Group_fk0" FOREIGN KEY ("artwork_title") REFERENCES "public.Artwork"("title");
ALTER TABLE "public.Artwork_Group" ADD CONSTRAINT "Artwork_Group_fk1" FOREIGN KEY ("group_name") REFERENCES "public.Group"("name");

ALTER TABLE "public.Customer_Group" ADD CONSTRAINT "Customer_Group_fk0" FOREIGN KEY ("customer_name") REFERENCES "public.Customer"("name");
ALTER TABLE "public.Customer_Group" ADD CONSTRAINT "Customer_Group_fk1" FOREIGN KEY ("group_name") REFERENCES "public.Group"("name");

ALTER TABLE "public.Customer_Artist" ADD CONSTRAINT "Customer_Artist_fk0" FOREIGN KEY ("artist_name") REFERENCES "public.Artist"("name");
ALTER TABLE "public.Customer_Artist" ADD CONSTRAINT "Customer_Artist_fk1" FOREIGN KEY ("customer_name") REFERENCES "public.Customer"("name");








