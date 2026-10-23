# R030FFG

## Descrição

Filial - FGTS

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpFgt | Date | Não | Competência do Fgts |
| RecFgt | Number(001,0) | Sim | Recolhimento FGTS (0,1,2) |
| CenFgt | Number(006,0) | Sim | Centralizadora do FGTS |
| CatFgt | Number(002,0) | Sim | Categoria FGTS |
| BanFgt | Number(004,0) | Sim | Banco do FGTS |
| AgeFgt | Number(005,0) | Sim | Agência do FGTS |
| EmpFgt | Number(013,0) | Sim | Empresa no FGTS |
| CdrFgt | Number(003,0) | Sim | Código de Recolhimento do Fgts (GFIP) |
| ModArq | Number(001,0) | Sim | Modalidade do Arquivo (GFip) |
| FunPro | String(020) | Sim | Número do fundo de provisão |
| UtiFin | String(001) | Sim | Utilização de recursos do FGTS em financiamentos |
| DebAut | String(001) | Sim | Débito automático do FGTS |
| AdeSMS | String(001) | Sim | Adesão aos Serviços de SMS |
| AgeRec | String(001) | Sim | Agendamento de recolhimento do FGTS |

---

## Chave Primária

- NumEmp
- CodFil
- CmpFgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030FFG_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

