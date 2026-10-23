# R038HCO

## Descrição

Histórico de Autorização de Desconto da Contribuição Sindical

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpAlt | Date | Não | Competência de Autorização de Desconto da Contribuição Sindical |
| CodSin | Number(004,0) | Sim | Código do Sindicato |
| CmpTer | Date | Sim | Validade da Autorização de Desconto da Contribuição Sindical |
| CtbSin | Number(001,0) | Sim | Contribuição Sindical no Ano |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAlt

---

## Índices

### R038HCOIndice2

**Tipo:** Não unico

Campos:
- CodSin

---

## Relacionamentos

### IR_R038HCO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

