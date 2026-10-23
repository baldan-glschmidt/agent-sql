# R195HAD

## Descrição

Cenário - Histórico Adicionais

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatAlt | Date | Não | Data de Início da Insalubridade do Colaborador |
| DatTer | Date | Sim | Data Término da Insalubridade do Colaborador |
| PerIns | Number(005,2) | Sim | % Insalubridade |
| PerPer | Number(005,2) | Sim | % Periculosidade |
| FatTpo | Number(004,2) | Sim | Fator Tempo Serviço |
| ApoEsp | Number(002,0) | Sim | Número de Anos p/ Aposentadoria Especial |
| GerCol | String(001) | Sim | Origem da geração do histórico |
| CmpTer | Date | Sim | Competência Término do Adicional |

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

### IR_R195HAD_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

