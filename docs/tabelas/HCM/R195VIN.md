# R195VIN

## Descrição

Cenário - Histórico Vínculo

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do Vínculo |
| CodVin | Number(002,0) | Sim | Tipo de Vínculo |
| GerCol | String(001) | Sim | Origem da geração do histórico |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195VIN_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195VIN_005

**Tabela:** R022VIN

| Origem | Destino |
|--------|---------|
| CodVin | CodVin |

