# R038HCT

## Descrição

Histórico Contratos

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatAlt | Date | Não | Data da alteração |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| NumCon | String(015) | Sim | Número do Contrato de Serviço |
| DatFim | Date | Sim | Data Final |
| StaAtu | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
