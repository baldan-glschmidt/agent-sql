# USU_TCadTer

## Descrição

Controle de integração de terceiros

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_NomOem | String(060) | Sim | Nome Outras Empresas |
| USU_NumCgc | String(014) | Não | CNPJ |
| USU_NumDoc | Number(011,0) | Não | CPF |
| USU_NomTer | String(040) | Sim | Nome |
| USU_DatRel | Date | Não | Data Integração |
| USU_DatVen | Date | Sim | Vencimento Integração |
| USU_Email | String(040) | Sim | E-mail |
| USU_AutAlm | String(001) | Sim | Autorização Almoço |
| USU_EnvEma | String(001) | Sim | Enviar e-mail? |
| USU_EndDoc | String(100) | Sim | Caminho Documento |
| USU_DatAso | Date | Sim | Data Validade Aso |

---

## Chave Primária

- USU_NumDoc
- USU_NumCgc
- USU_DatRel

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
