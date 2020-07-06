--
-- PostgreSQL database dump
--


--
-- TOC entry 7 (class 2615 OID 24587)
-- Name: STD; Type: SCHEMA; Schema: -; Owner: postgres
--

--CREATE SCHEMA "STD";

-- DROP TABLE

DROP TABLE IF EXISTS "STD".community_events cascade;
DROP TABLE IF EXISTS "STD".org_groups cascade;
DROP TABLE IF EXISTS "STD".organization_group_class cascade;
DROP TABLE IF EXISTS "STD".organizations cascade;
DROP TABLE IF EXISTS "STD".users cascade;




-- Name: users; Type: TABLE; Schema: STD; Owner: postgres
--

CREATE TABLE "STD".users (
    id bigint  NOT NULL,
    user_name character varying(55) NOT NULL,
    org_group_id bigint NOT NULL,
    password character varying(20),
    email character varying(55) NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id)
);

-- Name: organizations; Type: TABLE; Schema: STD; Owner: postgres

CREATE TABLE "STD".organizations (
    id bigint NOT NULL,
    name character varying(55) NOT NULL,
    city character varying(55) NOT NULL,
    state character varying(3) NOT NULL,
    zip_code integer NOT NULL,
    email character varying(55) NOT NULL,
    phone_number character varying(10) NOT NULL,
    org_type_class_id bigint NOT NULL,
    CONSTRAINT organizations_pkey PRIMARY KEY (id),
    CONSTRAINT zip_length CHECK ((zip_code <= 99999))
);


-- Name: org_groups; Type: TABLE; Schema: STD; Owner: postgres

CREATE TABLE "STD".org_groups (
    id bigint NOT NULL,
    name character varying(55) NOT NULL,
    organization_id bigint NOT NULL,
    city character varying(55) NOT NULL,
    state character varying(3) NOT NULL,
    zip_code integer NOT NULL,
    email character varying(55) NOT NULL,
    phone_number character varying(10) NOT NULL,
    
    CONSTRAINT org_groups_pkey PRIMARY KEY (id),
    CONSTRAINT zip_length CHECK ((zip_code <= 99999))
);

-- Name: organization_group_class; Type: TABLE; Schema: STD; Owner: postgres


CREATE TABLE "STD".organization_group_class (
    id integer NOT NULL,
    name character varying(55) NOT NULL,
    description text NOT NULL,
    
    CONSTRAINT organizations_group_class_pkey PRIMARY KEY (id)
);



-- Name: community_events; Type: TABLE; Schema: STD; Owner: postgres
--

CREATE TABLE "STD".community_events (
    id bigint NOT NULL,
    event_name character varying(55) NOT NULL,
    event_location character varying(75) NOT NULL,
    event_date date NOT NULL,
    event_time time NOT NULL,
    event_cost numeric(8,2),
    description text NOT NULL,
    address character varying(75) NOT NULL,
    city character varying(55) NOT NULL,
    state character varying(3) NOT NULL,
    zip_code integer NOT NULL,
    email character varying(55) NOT NULL,
    
     CONSTRAINT community_events_pkey PRIMARY KEY (id)
);





-- Name: organizations; Type: TABLE; Schema: STD; Owner: postgres

CREATE TABLE "STD".organizations (
    id bigint NOT NULL,
    name character varying(55) NOT NULL,
    city character varying(55) NOT NULL,
    state character varying(3) NOT NULL,
    zip_code integer NOT NULL,
    email character varying(55) NOT NULL,
    phone_number character varying(10) NOT NULL,
    org_type_class_id bigint NOT NULL,
    CONSTRAINT organizations_pkey PRIMARY KEY (id),
    CONSTRAINT zip_length CHECK ((zip_code <= 99999))
);









--- Foreign Keys

ALTER TABLE ONLY "STD".users
    ADD CONSTRAINT org_group_id_fk FOREIGN KEY (org_group_id) REFERENCES "STD".org_groups(id);

ALTER TABLE ONLY "STD".org_groups
    ADD CONSTRAINT org_id_fk FOREIGN KEY (organization_id) REFERENCES "STD".organizations(id);

ALTER TABLE ONLY "STD".organizations
    ADD CONSTRAINT org_type_class_id_fk FOREIGN KEY (org_type_class_id) REFERENCES "STD".organization_group_class(id);
   

--- Inserts 
INSERT INTO "STD".organization_group_class (id, name, description) VALUES (1, 'Health', 'A health orgnization');

INSERT INTO "STD".organizations (id, name, city, state, zip_code, email, phone_number, org_type_class_id) VALUES (1, 'main', 'rutherford', 'NY', 7070, 'geob3d@gmail.com', '2013973503', 1);





