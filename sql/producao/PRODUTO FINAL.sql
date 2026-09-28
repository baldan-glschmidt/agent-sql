
WITH produtos_encontrados AS (
    SELECT DISTINCT
           CONNECT_BY_ROOT a.codcmp AS produto_base,
           a.codemp,
           a.codmod,
           a.codder
    FROM e700ctm a,
         e075pro b,
         e075der c
    WHERE CONNECT_BY_ISLEAF = 1
      AND a.codemp = b.codemp
      AND a.codmod = b.codpro
      AND b.codemp = c.codemp
      AND b.codpro = c.codpro
      AND c.codder = a.codder
      AND b.sitpro = 'A'
      AND c.sitder = 'A'
    START WITH a.codcmp IN (
        SELECT pg.produto
        FROM produtos_goiania pg
    )
    CONNECT BY NOCYCLE
           PRIOR a.codmod = a.codcmp
       AND PRIOR a.codemp = a.codemp
),
produtos_com_origem AS (
    SELECT pe.*
    FROM produtos_encontrados pe
    JOIN e075pro p
      ON p.codemp = pe.codemp
     AND p.codpro = pe.codmod
    WHERE p.codori IN ('PLV', 'PPS', 'PLT', 'KAC')
)
SELECT pg.*,
       pe.codemp,
       pe.codmod,
       pe.codder,
       CASE
           WHEN pe.produto_base IS NULL THEN 'N'
           ELSE 'S'
       END AS USADO_PRODUTO_FINAL
FROM produtos_goiania pg
LEFT JOIN produtos_com_origem pe
  ON pe.produto_base = pg.produto
-- Para testar um produto específico, descomente:
 --WHERE pg.produto = '60203176743'
ORDER BY pg.produto, pe.codmod;
