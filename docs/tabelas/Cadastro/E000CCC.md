# E000CCC

## Descrição

Tabelas - Gerais - Controle de consumo de códigos diversos

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodCnm | String(050) | Não | Código passível de ser consumido. |
| NumSer | String(050) | Não | Número de série do código passível de ser consumido. |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodSer | String(014) | Sim | Código do serviço |
| CodSeg | Number(009,0) | Sim | Código da Seguradora |
| ValIni | Date | Sim | Data inicial de validade do código |
| ValFim | Date | Sim | Data final de validade do código |
| SitReg | String(001) | Sim | Situação do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E000CCC_UNIQUE

**Tipo:** Unico

Campos:
- CodCnm
- NumSer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
