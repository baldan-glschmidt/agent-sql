# E000IMP

## Descrição

Tabelas - Integrações - Alíquotas de Reduções Z

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal da redução Z |
| CroEcf | Number(006,0) | Não | Cont. de Reinício de Operação do ECF |
| DatRef | Date | Não | Data de referência da redução Z |
| CodStr | String(003) | Não | Código da situação tributária |
| AliImp | Number(015,4) | Sim | Alíquota do imposto da apuração |
| VltImp | Number(015,4) | Sim | Valor total da alíquota na redução Z |

---

## Chave Primária

- CodEmp
- CodFil
- CodEqu
- CroEcf
- DatRef
- CodStr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E000IMP_002

**Tabela:** E050EQF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodEqu | CodEqu |

