# R195PRC

## Descrição

Cenário - Programação de Férias Coletivas

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
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
| PrgDat | Date | Não | Data Início - Programação |
| PrgDfe | Number(004,2) | Sim | Dias Férias - Programação |
| PrgDab | Number(004,2) | Sim | Dias Abono - Programação |
| Prg13s | String(001) | Sim | Pagar 13° Salário - Programação |
| PrgDpg | Date | Sim | Data Pagto - Programação |
| GerAdt | String(001) | Sim | Gerar Adiantamento na Programação |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- PrgDat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195PRC_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

