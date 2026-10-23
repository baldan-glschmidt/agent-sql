# R047FAT

## Descrição

Definição de Faturas Integração ERP

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFat | Number(004,0) | Não | Código da definição da Fatura |
| NomFat | String(040) | Sim | Nome da Fatura |
| TipTis | String(003) | Sim | Tipo de Título do ERP |
| DiaNpg | Number(002,0) | Sim | Dia Normal de Pagamento |
| CodCif | Number(003,0) | Sim | Código de Integração Financeira |
| AbrEmp | String(100) | Sim | Abrangência de Empresas |
| AbrTcl | String(100) | Sim | Abrangencia de Tipo do Colaborador |
| AbrCad | String(100) | Sim | Abrangência de Cadastros |
| AbrFil | String(100) | Sim | Abrangência de Filiais |

---

## Chave Primária

- CodFat

---

## Índices

### R047FATIndice2

**Tipo:** Não unico

Campos:
- CodCif

---

## Relacionamentos

Nenhum relacionamento cadastrado.
