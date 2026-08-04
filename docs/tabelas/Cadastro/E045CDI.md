# E045CDI

## Descrição

Tabelas - Critério de Distribuição

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCri | Number(006,0) | Não | Código do critério |
| DesCri | String(100) | Sim | Descrição do critério |
| SitCri | String(001) | Sim | Situação do critério |
| DatAtu | Date | Sim | Data da última atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da última atualização do registro |

---

## Chave Primária

- CodEmp
- CodCri

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E045CDI_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

