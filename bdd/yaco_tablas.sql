CREATE TABLE "USUARIO"
(
    "usu_id"             varchar(30) NOT NULL,
    "usu_pass"           varchar(20) NOT NULL,
    "usu_fecha_registro" date NOT NULL,
    CONSTRAINT "PK_USUARIO" PRIMARY KEY ( "usu_id" )
);

CREATE TABLE "LOGIN"
(
    "log_id"             varchar(50) NOT NULL,
    "usu_id"             varchar(30) NOT NULL,
    "log_fecha"          date NOT NULL,
    CONSTRAINT "PK_LOGIN" PRIMARY KEY ( "log_id" ),
    CONSTRAINT "FK_USU_ID" FOREIGN KEY ( "usu_id" ) REFERENCES "USUARIO" ( "usu_id" )
);

CREATE TABLE "ESTUDIANTE"
(
    "usu_id"             varchar(30) NOT NULL,
    "est_tipo"           varchar(20) NOT NULL,
    CONSTRAINT "PK_ESTUDIANTE" PRIMARY KEY ( "usu_id" ),
    CONSTRAINT "FK_USU" FOREIGN KEY ( "usu_id" ) REFERENCES "USUARIO" ( "usu_id" ) 
);

CREATE TABLE "PALABRA"
(
    "pal_id"             varchar(20) NOT NULL,
    "usu_id"             varchar(30) NOT NULL,
    "pal_tipo"           varchar(50) NOT NULL,
    "pal_es_ofensiva"    boolean NOT NULL,
    CONSTRAINT "PK_PALABRA" PRIMARY KEY ( "pal_id", "usu_id" ),
    CONSTRAINT "FK_FC" FOREIGN KEY ( "usu_id" ) REFERENCES "ESTUDIANTE" ( "usu_id" )
);

CREATE TABLE "DEFINICION"
(
    "def_id"             varchar(20) NOT NULL,
    "pal_id"             varchar(20) NOT NULL,
    "usu_id"             varchar(30) NOT NULL,
    "def_definicion"     varchar(50) NOT NULL,
    "def_info_adicional" text NOT NULL,
    "def_idioma"         varchar(10) NOT NULL,
    CONSTRAINT "PK_DEFINICION" PRIMARY KEY ( "def_id", "pal_id", "usu_id" ),
    CONSTRAINT "FK_PAL" FOREIGN KEY ( "pal_id" ) REFERENCES "PALABRA" ( "pal_id" ),
    CONSTRAINT "FK_USU" FOREIGN KEY ( "usu_id" ) REFERENCES "PALABRA" ( "usu_id" )
);

CREATE TABLE "FLASHCARD"
(
    "fla_id"             varchar(20) NOT NULL,
    "fla_fecha_creacion" date NOT NULL,
    "fla_nivel_srs_reco" int NOT NULL,
    "fla_nivel_srs_prod" int NOT NULL,
    "pal_id"             varchar(20) NOT NULL,
    "usu_id"             varchar(30) NOT NULL,
    CONSTRAINT "PK_FLASHCARD" PRIMARY KEY ( "fla_id" ),
    CONSTRAINT "FK_PAL_ID" FOREIGN KEY ( "pal_id" ) REFERENCES "PALABRA" ( "pal_id" ),
    CONSTRAINT "FK_USU_ID" FOREIGN KEY ( "usu_id" ) REFERENCES "ESTUDIANTE" ( "usu_id" )
);

CREATE TABLE "REVISION"
(
    "rev_id"             varchar(20) NOT NULL,
    "fla_id"             varchar(20) NOT NULL,
    "fla_fecha"          date NOT NULL,
    "fla_es_completa"    boolean  NOT NULL,
    "fla_equivocacion_previa" boolean NOT  NULL,
    "nivel_srs"          int NOT NULL,
    CONSTRAINT "PK_REVISION" PRIMARY KEY ( "rev_id", "fla_id" ),
    CONSTRAINT "FK_FLA_ID" FOREIGN KEY ( "fla_id" ) REFERENCES "FLASHCARD" ( "fla_id" ) 
);