DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE IF NOT EXISTS "USUARIO"
(
    "usu_id"             varchar(30) NOT NULL,
    "usu_pass"           varchar(20) NOT NULL,
    "usu_fecha_registro" date NOT NULL,
    CONSTRAINT "PK_USUARIO" PRIMARY KEY ( "usu_id" )
);

CREATE TABLE IF NOT EXISTS "LOGIN"
(
    "log_id"             varchar(50) NOT NULL,
    "usu_id"             varchar(30) NOT NULL,
    "log_fecha"          date NOT NULL,
    CONSTRAINT "PK_LOGIN" PRIMARY KEY ( "log_id" ),
    CONSTRAINT "FK_USU_ID" FOREIGN KEY ( "usu_id" ) REFERENCES "USUARIO" ( "usu_id" ) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "ESTUDIANTE"
(
    "usu_id"             varchar(30) NOT NULL,
    "est_tipo"           varchar(20) NOT NULL,
    CONSTRAINT "PK_ESTUDIANTE" PRIMARY KEY ( "usu_id" ),
    CONSTRAINT "FK_USU" FOREIGN KEY ( "usu_id" ) REFERENCES "USUARIO" ( "usu_id" ) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "PALABRA"
(
    "pal_id"             varchar(50) NOT NULL,
    "pal_tipo"           varchar(50) NOT NULL,
    "pal_es_ofensiva"    boolean NOT NULL,
    CONSTRAINT "PK_PALABRA" PRIMARY KEY ( "pal_id")
);

CREATE TABLE IF NOT EXISTS "USUARIO_PALABRA"
(
    "usu_id"             varchar(30) NOT NULL,
    "pal_id"           varchar(50) NOT NULL,
    CONSTRAINT "PK_USUARIO_PALABRA" PRIMARY KEY ( "usu_id", "pal_id" ),
    CONSTRAINT "FK_USU" FOREIGN KEY ( "usu_id" ) REFERENCES "ESTUDIANTE" ( "usu_id" ) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "FK_PAL" FOREIGN KEY ( "pal_id" ) REFERENCES "PALABRA" ( "pal_id" ) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "DEFINICION"
(
    "def_id"             varchar(60) NOT NULL,
    "def_definicion"     varchar(50) NOT NULL,
    "def_idioma"         varchar(10) NOT NULL,
    "def_info_adicional" text NOT NULL,
    "def_principal"      boolean NOT NULL,
    "def_extra"          boolean NOT NULL,
    CONSTRAINT "PK_DEFINICION" PRIMARY KEY ( "def_id" )
);

CREATE TABLE IF NOT EXISTS "PALABRA_DEFINICION"
(
    "pal_id"             varchar(50) NOT NULL,
    "def_id"             varchar(60) NOT NULL,
    CONSTRAINT "PK_PALABRA_DEFINICION" PRIMARY KEY ( "pal_id", "def_id" ),
    CONSTRAINT "FK_PAL" FOREIGN KEY ( "pal_id" ) REFERENCES "PALABRA" ( "pal_id" ) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "FK_DEF" FOREIGN KEY ( "def_id" ) REFERENCES "DEFINICION" ( "def_id" ) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "FLASHCARD"
(   
    "fla_id"             varchar(60) NOT NULL,
    "fla_tipo"           varchar(10) NOT NULL,
    "fla_nivel_srs"      int NOT NULL,
    CONSTRAINT "PK_FLASHCARD" PRIMARY KEY ( "fla_id" )
);

CREATE TABLE IF NOT EXISTS "USU_PAL_FLASHCARD"
(
    "usu_id"             varchar(30) NOT NULL,
    "pal_id"             varchar(50) NOT NULL,
    "fla_id"             varchar(60) NOT NULL,
    "fla_fecha_creacion" date NOT NULL,
    CONSTRAINT "PK_USU_PAL_FLASHCARD" PRIMARY KEY ( "usu_id", "pal_id", "fla_id" ),
    CONSTRAINT "FK_USU" FOREIGN KEY ( "usu_id" ) REFERENCES "ESTUDIANTE" ( "usu_id" ) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "FK_PAL" FOREIGN KEY ( "pal_id" ) REFERENCES "PALABRA" ( "pal_id" ) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "FK_FLA" FOREIGN KEY ( "fla_id" ) REFERENCES "FLASHCARD" ( "fla_id" ) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "REVISION"
(
    "rev_id"             varchar(60) NOT NULL,
    "rev_es_completa"    boolean  NOT NULL,
    "rev_equivocacion_previa" boolean NOT  NULL,
    "rev_nivel_srs"          int NOT NULL,
    CONSTRAINT "PK_REVISION" PRIMARY KEY ( "rev_id")
);

CREATE TABLE IF NOT EXISTS "FLASHCARD_REVISION"
(
    "rev_id"             varchar(60) NOT NULL,
    "fla_id"           varchar(60) NOT NULL,
    "fla_fecha"          date NOT NULL,
    CONSTRAINT "PK_FLA_REV" PRIMARY KEY ( "rev_id", "fla_id" ),
    CONSTRAINT "FK_REV" FOREIGN KEY ( "rev_id" ) REFERENCES "REVISION" ( "rev_id" ) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "FK_FLA" FOREIGN KEY ( "fla_id" ) REFERENCES "FLASHCARD" ( "fla_id" ) ON DELETE CASCADE ON UPDATE CASCADE
);