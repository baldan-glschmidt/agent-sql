# E037TDC

## Descrição

Tabelas - Taxa por Dias a Compensar

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| QdtDia | Number(003,0) | Não | Quantidade de dias para compensação |
| VlrTax | Number(007,4) | Não | Taxa cobrada no período de compensação |
| DesTax | String(030) | Sim | Descrição da taxa cobrada |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- QdtDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E037TDC_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

