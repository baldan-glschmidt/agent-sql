# R195PRG

## Descrição

Cenário - Programação Férias

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| IniPer | Date | Não | Início do Período Aquisitivo |
| PrgDat | Date | Não | Data Início - Programação |
| PrgDfe | Number(004,2) | Sim | Dias Férias - Programação |
| PrgDab | Number(004,2) | Sim | Dias Abono - Programação |
| Prg13s | String(001) | Sim | Pagar 13° Salário - Programação |
| PrgDpg | Date | Sim | Data Pagto - Programação |
| PrgPcl | Number(002,0) | Sim | Número de Parcelas de Desconto - Programação |
| GerAdt | String(001) | Sim | Gerar Adiantamento na Programação |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- IniPer
- PrgDat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195PRG_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

