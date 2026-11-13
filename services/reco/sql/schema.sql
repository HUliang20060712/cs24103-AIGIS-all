-- AIGIS B-推荐系统 5 张表（M3 冻结）
CREATE TABLE IF NOT EXISTS preference (
  user_id     BIGINT       NOT NULL,
  categories  VARCHAR(128) NOT NULL,
  weight      NUMERIC(3,2) NOT NULL DEFAULT 0.50,
  updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS item_meta (
  item_id     BIGINT       PRIMARY KEY,
  name        VARCHAR(64)  NOT NULL,
  category    VARCHAR(16)  NOT NULL,
  lon         NUMERIC(9,6),
  lat         NUMERIC(9,6),
  tags        VARCHAR(128),
  updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_item_category ON item_meta (category);

CREATE TABLE IF NOT EXISTS interaction (
  id          BIGSERIAL    PRIMARY KEY,
  user_id     BIGINT       NOT NULL,
  item_id     BIGINT       NOT NULL,
  action      VARCHAR(12)  NOT NULL,
  occurred_at TIMESTAMPTZ  NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_interaction_user ON interaction (user_id, occurred_at DESC);

CREATE TABLE IF NOT EXISTS feedback (
  id          BIGSERIAL    PRIMARY KEY,
  user_id     BIGINT       NOT NULL,
  item_id     BIGINT       NOT NULL,
  action      VARCHAR(12)  NOT NULL,
  created_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS hot_rank (
  category    VARCHAR(16)  NOT NULL,
  item_id     BIGINT       NOT NULL,
  score       NUMERIC(6,3) NOT NULL,
  stat_date   DATE         NOT NULL,
  PRIMARY KEY (category, item_id, stat_date)
);
