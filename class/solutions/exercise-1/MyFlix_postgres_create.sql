CREATE TABLE "public.Movies" (
	"movie_id" serial NOT NULL,
	"title" TEXT NOT NULL,
	"director" TEXT NOT NULL,
	"year_released" integer NOT NULL,
	"category" integer NOT NULL,
	CONSTRAINT "Movies_pk" PRIMARY KEY ("movie_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Categories" (
	"category_id" serial NOT NULL,
	"category_name" TEXT NOT NULL,
	"remarks" TEXT NOT NULL,
	CONSTRAINT "Categories_pk" PRIMARY KEY ("category_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Members" (
	"membership_no" serial NOT NULL,
	"full_names" TEXT NOT NULL,
	"gender" TEXT NOT NULL,
	"date_of_birth" DATE NOT NULL,
	"physical_adress" TEXT NOT NULL,
	"postal_adress" TEXT NOT NULL,
	CONSTRAINT "Members_pk" PRIMARY KEY ("membership_no")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Payments" (
	"payment_id" serial NOT NULL,
	"membership_no" integer NOT NULL,
	"payment_date" DATE NOT NULL,
	"description" TEXT NOT NULL,
	"amount_paid" integer NOT NULL,
	CONSTRAINT "Payments_pk" PRIMARY KEY ("payment_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Movie Rentals" (
	"reference_no" serial NOT NULL,
	"transaction_date" DATE NOT NULL,
	"membership_id" integer NOT NULL,
	"movie_id" integer NOT NULL,
	"return_date" DATE NOT NULL,
	CONSTRAINT "Movie Rentals_pk" PRIMARY KEY ("reference_no")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "Movies" ADD CONSTRAINT "Movies_fk0" FOREIGN KEY ("category") REFERENCES "Categories"("category_id");



ALTER TABLE "Payments" ADD CONSTRAINT "Payments_fk0" FOREIGN KEY ("membership_no") REFERENCES "Members"("membership_no");

ALTER TABLE "Movie Rentals" ADD CONSTRAINT "Movie Rentals_fk0" FOREIGN KEY ("membership_id") REFERENCES "Members"("membership_no");
ALTER TABLE "Movie Rentals" ADD CONSTRAINT "Movie Rentals_fk1" FOREIGN KEY ("movie_id") REFERENCES "Movies"("movie_id");





